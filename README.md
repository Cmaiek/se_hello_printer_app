# Simple Flask App 
[![Build Status](https://travis-ci.com/Cmaiek/se_hello_printer_app.svg?branch=master)](https://travis-ci.com/Cmaiek/se_hello_printer_app)

[![Uptime Status](https://app.statuscake.com/button/index.php?Track=6003142&Days=1&Design=2)](app.statuscake.com)

Aplikacja Dydaktyczna wyświetlająca imię i wiadomość w różnych formatach dla zajęć
o Continuous Integration, Continuous Delivery i Continuous Deployment.

- W projekcie wykorzystamy virtual environment, dla utworzenia hermetycznego środowisko dla aplikacji:

  ```
  # tworzymy hermetyczne środowisko dla bibliotek aplikacji:
  $ python3 -m venv .venv

  # aktywowanie hermetycznego środowiska
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  $ pip install -r test_requirements.txt

  # zobacz
  $ pip list
  ```

  Sprawdź: [tutorial venv](https://docs.python.org/3/tutorial/venv.html) oraz [biblioteki flask](http://flask.pocoo.org).

- Uruchamianie applikacji:

  ```
  # jako zwykły program
  $ python main.py

  # albo:
  $ PYTHONPATH=. FLASK_APP=hello_world flask run
  ```

- Uruchamianie testów (see: http://doc.pytest.org/en/latest/capture.html):

  ```
  $ PYTHONPATH=. py.test
  $ PYTHONPATH=. py.test --verbose -s
  ```

- Kontynuując pracę z projektem, aktywowanie hermetycznego środowiska dla aplikacji py:

  ```
  # deaktywacja
  $ deactivate
  ```

  ```
  ...

  # aktywacja 
  $ source .venv/bin/activate
  ```

- Integracja z TravisCI:

  ```
  # miejsce na twoje notatki
  ```


- Aplikacja jest monitorowana za pomocą statuscake.com
Odpytywanie co 5 minut z losowych lokalizacji, w przypadku wyłączenia aplikacji powiadomienie mailowe do grupy szybkiego reagowania
# Pomocnicze

## Ubuntu

- Instalacja dockera: [dockerce howto](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

## Centos

- Instalacja docker-a:

  ```
  $ yum remove docker \
        docker-common \
        container-selinux \
        docker-selinux \
        docker-engine

  $ yum install -y yum-utils

  $ yum-config-manager \
      --add-repo \
      https://download.docker.com/linux/centos/docker-ce.repo

  $ yum makecache fast
  $ yum install -y docker-ce
  $ systemctl start docker
  ```
