## Steps to setup project

### nest (scrapy project, crawler is ```soda```)

- modify MySQL settings
- setup cron job
  - run ```crontab -e```
  - add following line
  ```
  @daily /path/scrapy crawl soda
  ```

### webapps (dashboard)

- modify MySQL settings
- python manage.py migrate
- yarn install
- gulp vendor
- python manage.py runserver

