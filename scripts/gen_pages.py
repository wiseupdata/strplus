import os 
import sys 
os.path.abspath(".")

package_name = "strplus"

from pathlib import Path
import mkdocs_gen_files

src_root = Path("strplus")
for path in src_root.glob("**/*.py"):
    doc_path = Path(package_name, path.relative_to(src_root)).with_suffix(".md")
    
    with mkdocs_gen_files.open(doc_path, "w") as f:
        ident = ".".join(path.with_suffix("").parts)
        print("::: " + ident, file=f)
        
        