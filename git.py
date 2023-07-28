import subprocess
lien = "https://github.com/jojo8356/verification_and_save_new_python_file_save.git"
key = "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"
lien_split = lien.split("https://")
nw_lien = "https://"+key+"@"+lien_split[1]
commit = "1er commit"
commands = f"""echo "# Project" >> README.md
git init
git add .
git commit -m "{commit}"
git branch -M main
git remote add origin {nw_lien}
git push -u origin main"""
print(commands)
subprocess.run(commands, shell=True)

