# %%
# from importlib import reload
from uuid import uuid4
from matplotlib import pyplot as plt
import venn

# help(venn)
# reload(venn)
# plt.title("test_demo")
# plt.text(0, -0.1, "test2_demo", ha='center', ma='left',
#          url="https://www.baidu.com/s?ie=UTF-8&wd=test",
#          bbox=dict(url="https://www.baidu.com/s?ie=UTF-8&wd=test", alpha=0.001,)
#          )
upload_key = str(uuid4())
outdir = "uploadr/static/uploads/{}".format(upload_key)
outdir


L = [('Aname', 'a'), ('A', '1\r\n2\r\n3'), ('Bname', 'b'), ('B', '1\r\n2\r\n3\r\n4'), ('Cname', 'c'),
     ('C', '1\r\n2\r\n'), ('Dname', ''), ('D', ''), ('Ename', ''), ('E', ''), ('Fname', ''), ('F', '')]
D = dict(zip([x[1] for x in L[0::2] if x[1]],
             [{xx.strip() for xx in x[1].split("\n")} for x in L[1::2] if x[1]]))
D
ax, outname = venn.venn(D,
                        fmt="{percentage:.1f}%\n({size})",
                        figsize=(9, 9),
                        fontsize=12,
                        outdir=outdir,
                        #   alpha=.5,
                      #  cmap=["r", "g", "b"]
                        #  cmap="Accent"
                        #  cmap="Set2"  # 蓝 绿 紫
                        #  cmap="Set3"  # 蓝 绿 黄
                        #  cmap=list("rgy")  # 红 绿 黄
                        cmap=list("rgby")  # 红 绿 黄
                        )
svgurl = f"./uploadr/static/uploads/2a9918af-b1ec-4fd3-bdc3-1a7e00daeddb/{outname}venn.svg"

# @app.route('/result')
# def svgview(upload_key):
#     pass

# %%
inset = {"A-set": {1, 2, 3},
         "B-set": {1, 2, 3, 4},
         "C-set-demo": {1, 2, 3, 4, 5, 6, 7, 8, 9, 0},
         #  "D":{99, 100},
         #  "E":{99, 100},
         }
ax, outname = venn.venn(inset,
                        fmt="{percentage:.1f}%\n({size})",
                        figsize=(9, 9),
                        fontsize=12,
                        outdir="out-test",
                        #   alpha=.5,
                        #  cmap=["r", "g", "b"]
                        #  cmap="Accent"
                        #  cmap="Set2"  # 蓝 绿 紫
                        #  cmap="Set3"  # 蓝 绿 黄
                        #  cmap=list("rgy")  # 红 绿 黄
                        cmap=list("rgby")  # 红 绿 黄
                        )

# %%

ax, outname = venn.venn({"A-set": {1, 2, 3},
                         "B-set": {1, 2, 3, 4},
                         "C-set-demo": {1, 2, 3, 4, 5, 6, 7, 8, 9, 0},
                         "D": {99, 100},
                         #  "E":{99, 100},
                         },
                        fmt="{percentage:.1f}%\n({size})",
                        figsize=(9, 9),
                        fontsize=12,
                        outdir="out-test",
                        #   alpha=.5,
                        #  cmap=["r", "g", "b"]
                        #  cmap="Accent"
                        #  cmap="Set2"  # 蓝 绿 紫
                        #  cmap="Set3"  # 蓝 绿 黄
                        #  cmap=list("rgy")  # 红 绿 黄
                        # cmap=list("rgby")  # 红 绿 黄
                        )
# plt.savefig(f'{outname}venn.pdf', dpi=200, bbox_inches='tight')
# plt.savefig(f'{outname}venn.png', dpi=200, bbox_inches='tight')
# plt.savefig(f'{outname}venn.svg', dpi=200, bbox_inches='tight')
