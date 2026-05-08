#!/usr/bin/env python3
"""将 HS 各年份 JSON 数据文件转换为浏览器可加载的 JS 文件。

用法:
    python3 convert.py                  # 转换当前目录下所有 HS2*.json
    python3 convert.py HS2007.json      # 只转换指定文件
"""

import json, os, sys, glob

def convert(input_file, output_dir="."):
    base = os.path.splitext(os.path.basename(input_file))[0]   # HS2002
    var_name = base.upper().replace("-", "_") + "_DATA"        # HS2002_DATA
    output = os.path.join(output_dir, f"{base.lower()}-data.js")

    with open(input_file, encoding="utf-8") as f:
        data = json.load(f)

    with open(output, "w", encoding="utf-8") as f:
        f.write(f"var {var_name} = ")
        json.dump(data["results"], f, separators=(",", ":"))
        f.write(";\n")

    print(f"OK  {input_file}  ->  {output}  ({len(data['results'])} items)")

if __name__ == "__main__":
    files = sys.argv[1:] if len(sys.argv) > 1 else glob.glob("HS*.json")
    if not files:
        print("未找到 HS*.json 文件。")
        sys.exit(1)
    for f in sorted(files):
        convert(f)
