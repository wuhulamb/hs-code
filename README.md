# HS 海关编码浏览器

基于海关编码（HS Code）JSON 数据生成的交互式树形浏览器，可在浏览器中直观地浏览、搜索各级海关编码。支持 HS 多年度版本。

## 文件组成

| 文件 | 说明 |
|------|------|
| `HS1992.json` ~ `HS2022.json` | 原始海关编码 JSON 数据（7 个版本） |
| `hs*-data.js` | 转换产物，给浏览器加载的数据文件 |
| `convert.py` | 通用转换脚本，将 `HS*.json` 转换为浏览器可加载的 JS 数据文件 |
| `index.html` | 版本选择首页，列出所有可用 HS 版本 |
| `viewer.html` | 通用查看器，通过 URL 参数 `?edition=hs2022` 加载不同版本数据 |
| `README.md` | 本说明文件 |

## 使用方法

打开 `index.html` 选择版本，或直接打开 `viewer.html?edition=hs2002` 查看特定版本。

无需任何服务器或构建工具，直接用浏览器打开即可。

### 数据层级

编码按 4 个聚合级别组织：

| 层级 | 含义 | 示例 |
|------|------|------|
| Level 0 | 总计（根节点） | Total - All H2 Commodities |
| Level 2 | 章（2 位编码） | 01 - Live animals |
| Level 4 | 目（4 位编码） | 0101 - Live horses, asses, mules and hinnies |
| Level 6 | 子目（6 位编码，叶子节点） | 010110 - Pure-bred breeding animals |

### 功能

- **展开/折叠** — 点击任意节点展开或收起其子项
- **搜索** — 按编码或描述搜索，自动高亮匹配项并展开路径
- **展开/收起全部** — 一键展开或收起整个树

## 可用版本

| 版本 | 条目数 |
|------|--------|
| HS1992 | 6382 |
| HS1996 | 6475 |
| HS2002 | 6570 |
| HS2007 | 6374 |
| HS2012 | 6530 |
| HS2017 | 6709 |
| HS2022 | 6940 |

## 数据来源

HS（Harmonized System）是海关合作理事会（WCO）制定的《商品名称及编码协调制度》。

原始 JSON 数据可从联合国统计司下载：[https://unstats.un.org/unsd/classifications/Econ](https://unstats.un.org/unsd/classifications/Econ)

## 添加新版本

将新的 JSON 文件放入项目目录（如 `HS2027.json`），然后运行：

```bash
python3 convert.py                  # 转换所有 HS*.json
python3 convert.py HS2027.json      # 或只转换指定文件
```

脚本会为每个 JSON 生成对应的 `*-data.js` 文件。然后打开 `index.html` 即可看到新版本入口。

如果新版本未自动显示在首页，编辑 `index.html` 中的 `editions` 数组手动添加：

```javascript
const editions = [
  { id: 'hs1992', label: 'HS1992', desc: '1992 年版' },
  { id: 'hs1996', label: 'HS1996', desc: '1996 年版' },
  { id: 'hs2002', label: 'HS2002', desc: '2002 年版' },
  { id: 'hs2007', label: 'HS2007', desc: '2007 年版' },
  { id: 'hs2012', label: 'HS2012', desc: '2012 年版' },
  { id: 'hs2017', label: 'HS2017', desc: '2017 年版' },
  { id: 'hs2022', label: 'HS2022', desc: '2022 年版' },
];
```
