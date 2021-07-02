# Hello World Printer
## To-do / next steps

W celu zapewnienia i utrzymania jakości oprogramowania, w przyszłości do procesu CI/CD należy dołączyć dodatkowe testy.

1. Testy wydajności
Należy dodać testy oraz monitorowanie wydajności za pomocą **locust**, w celu okresowej oceny wydajności stosowanego dyno w __Heroku.com__. W przypadku wzrostu ruchu w aplikacji bądź obniżenia rzeczywistych parametrów dyno, należy rozważyć przejście na wyższą taryfę bądź zmianę providera PaaS (np. na DigitalOcean App Platform, które działa na engine'nie Heroku, dzięki czemu migracja byłaby stosunkowo najmniej kosztowna).

Test siłą rzeczy musi zostać przeprowadzony po fazie deploymentu do Heroku. Zaleca się utworzenie odrębnej instancji (na identycznych parametrach dyno), w celu uniknięcia testów na produkcji.

2. Testy bezpieczeństwa
Jeżeli aplikacja zostanie w przyszłości wyposażona w funkcje wymagające zbierania i przetwarzania danych (np. zakładanie kont przez użytkowników), wersja produkcyjna aplikacji powinna być okresowo testowana pod kątem bezpieczeństwa (np. za pomocą narzędzi z dystrybucji Kali Linux, takich jak Nmap). Należy rozważyć wynajęcie do tego zadania zewnętrznych testerów penetracyjnych.

3. Vulnerability testing
Vulnerabiity testing to testowanie kodu pod kątem wykorzystania bibliotek i komponentów, w których ujawnione zostały podatności na atak. W procesie CI/CD HWP, test ten może zostać przeprowadzony na obrazie Dockera wgranym każdorazowo do hub.docker.com. 