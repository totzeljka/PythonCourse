

# pipenv
# u cmd kucam pip3 install pipenv

# u terminalu vskoda kucam pipenv install requests, instalirace mi enviroment  i videcu dva nova fajla Pipfile i Pipfile.lock
# da bih videla env kucam u terminalu:   pipenv --venv i kao responce dobijem put do virtuelnog enviromenta  :
# C:\Users\zeljka.tot\.virtualenvs\PythonCourse-jjRvJAC9
# PS C:\Users\zeljka.tot\PythonCourse>

# u terminalu kuca, pipenv shell

#     Launching subshell in virtual environment...
# PowerShell 7.3.4

#    A new PowerShell stable release is available: v7.3.5
#    Upgrade now, or check out the release page at:
#      https://aka.ms/PowerShell-Release?tag=v7.3.5

# da izadjemo kucam u terminalu exit


# ako nemamo taj environment tipa dobijem kod od nekog drugog kucam u cmd pipenv install --ignore-pipfile
# tada ce instalirati dependensie koji su sacuvani u pipfile.lock

# u terminalu kucam: pipenv graph da vidimo sve instalirane dependensie
# ja dobijem:
# requests==2.31.0
# ├── certifi [required: >=2017.4.17, installed: 2023.5.7]
# ├── charset-normalizer [required: >=2,<4, installed: 3.1.0]
# ├── idna [required: >=2.5,<4, installed: 3.4]
# └── urllib3 [required: >=1.21.1,<3, installed: 2.0.3]

# da se nadju outdatirani paketi  kucam u terminalu: pipenv update --outdated
# da se uninstalira requests paket u terminalu kucam pipenv uninstall requests i u pipfajlu vise nema nista
