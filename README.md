# pytest-web

# Local

pip install -r requirements.txt

python runner.py - run

python runner.py - generate_report

python runner.py - open_report

python runner.py - generate_report - open_report

python runner.py - run - generate_report - open_report

# Remote

1. Install NodeJs.
2. Install selenium-standalone package.
   https://www.npmjs.com/package/selenium-standalone

```commandline
npm install selenium-standalone -g

selenium-standalone install

selenium-standalone start
```

3. Add selenium_server to [environment.properties](environment.properties) such as:

```commandline
selenium_server=http://localhost:4444/wd/hub
```

4. python runner.py - run - generate_report - open_report

Or:

1. Install Java.
2. Download selenium jar and start grid/hub
   https://www.selenium.dev/downloads/
3. Add selenium_server to [environment.properties](environment.properties) such as:

```commandline
selenium_server=http://localhost:4444/wd/hub
```

4. python runner.py - run - generate_report - open_report