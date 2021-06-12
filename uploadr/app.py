from flask import Flask, request, redirect, url_for, render_template
import os
import json
import glob
from uuid import uuid4
import venn


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/pyveen')
def pyveen():
    return render_template('pyveen.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        upload_key = str(uuid4())
        outdir = "uploadr/static/uploads/{}".format(upload_key)
        results = request.form
        L = list(results.items())
        # D = dict(zip([x[1] for x in L[0::2] if x[1]],
        #              [{xx.strip() for xx in x[1].strip().split("\n") if xx.strip()}
        #               for x in L[1::2] if x[1]]))
        # print(L)
        D = {}
        for name, data in zip(L[0::2], L[1::2]):
            k = name[1].strip()
            w = data[1].strip().replace("\r", "")
            # print(k)
            if not k and not w:
                break
            tmp_set = set()
            for x in w.split("\n"):
                if x.strip():
                    # print(tmp_set)
                    tmp_set.add(x.strip())
            if tmp_set:
                D[k] = tmp_set
        # print(D)
        ax, outname = venn.venn(D,
                                fmt="{percentage:.1f}%\n({size})",
                                figsize=(9, 9),
                                fontsize=12,
                                outdir=outdir,
                                # cmap=list("rgby")  # 红 绿 黄
                                )
        svgurl = f"/uploads/{upload_key}/{outname}venn.svg"

        return render_template("svgview.html", svgurl=svgurl)


@app.route("/upload", methods=["POST"])
def upload():
    """Handle the upload of a file."""
    form = request.form

    # Create a unique "session ID" for this particular batch of uploads.
    upload_key = str(uuid4())

    # Is the upload using Ajax, or a direct POST by the form?
    is_ajax = False
    if form.get("__ajax", None) == "true":
        is_ajax = True

    # Target folder for these uploads.
    target = "uploadr/static/uploads/{}".format(upload_key)
    try:
        os.mkdir(target)
    except:
        if is_ajax:
            return ajax_response(False, "Couldn't create upload directory: {}".format(target))
        else:
            return "Couldn't create upload directory: {}".format(target)

    print("=== Form Data ===")
    for key, value in list(form.items()):
        print(key, "=>", value)

    for upload in request.files.getlist("file"):
        filename = upload.filename.rsplit("/")[0]
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)

    if is_ajax:
        return ajax_response(True, upload_key)
    else:
        return redirect(url_for("upload_complete", uuid=upload_key))


@app.route("/files/<uuid>")
def upload_complete(uuid):
    """The location we send them to at the end of the upload."""

    # Get their files.
    root = "uploadr/static/uploads/{}".format(uuid)
    if not os.path.isdir(root):
        return "Error: UUID not found!"

    files = []
    for file in glob.glob("{}/*.*".format(root)):
        fname = file.split(os.sep)[-1]
        files.append(fname)

    return render_template("files.html",
        uuid=uuid,
        files=files,
    )


def ajax_response(status, msg):
    status_code = "ok" if status else "error"
    return json.dumps(dict(
        status=status_code,
        msg=msg,
    ))
