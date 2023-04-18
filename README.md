Установите Java на вашей системе, если она еще не установлена. Для установки Java можно посетить официальный сайт Oracle (https://www.oracle.com/java/technologies/javase-jdk8-downloads.html) и следовать инструкциям.  
Скачайте Selenium Standalone Server с официального сайта Selenium (https://www.selenium.dev/downloads/). Распакуйте архив в удобное для вас место на вашем компьютере.  
Скачайте ChromeDriver с официального сайта Chromium (https://sites.google.com/a/chromium.org/chromedriver/downloads) в соответствии с версией Google Chrome, установленной на вашем компьютере. Распакуйте драйвер в удобное для вас место на вашем компьютере.  
Замените path-to-chromedriver и path-to-selenium.jar на пути к файлам ChromeDriver и Selenium Standalone Server  
Выполните следующую команду в командной строке, чтобы запустить сервер Selenium Standalone:  
`java "-Dselenium.LOGGER.level=OFF" "-Xmx512m" "-Dwebdriver.chrome.driver=path-to-chromedriver" -jar path-to-selenium.jar standalone --port 4444`
