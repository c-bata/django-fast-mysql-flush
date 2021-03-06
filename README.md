# README

for Django ticket #31275

## setup database

```
$ docker run \
  -d \
  --rm \
  -p 3306:3306 \
  -e MYSQL_USER=django \
  -e MYSQL_DATABASE=django \
  -e MYSQL_PASSWORD=password \
  -e MYSQL_ALLOW_EMPTY_PASSWORD=yes \
  --name django-mysql \
  mysql:8.0

$ python manage.py migrate
...
```

## Tables

```
$ mysql --host 127.0.0.1 --port 3306 --user django -ppassword -e "show tables";
+----------------------------+
| Tables_in_django           |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
| hello_question0            |
| hello_question1            |
| hello_question10           |
| hello_question11           |
| hello_question12           |
| hello_question13           |
| hello_question14           |
| hello_question15           |
| hello_question16           |
| hello_question17           |
| hello_question18           |
| hello_question19           |
| hello_question2            |
| hello_question20           |
| hello_question21           |
| hello_question22           |
| hello_question23           |
| hello_question24           |
| hello_question25           |
| hello_question26           |
| hello_question27           |
| hello_question28           |
| hello_question29           |
| hello_question3            |
| hello_question30           |
| hello_question31           |
| hello_question32           |
| hello_question33           |
| hello_question34           |
| hello_question35           |
| hello_question36           |
| hello_question37           |
| hello_question38           |
| hello_question39           |
| hello_question4            |
| hello_question40           |
| hello_question41           |
| hello_question42           |
| hello_question43           |
| hello_question44           |
| hello_question45           |
| hello_question46           |
| hello_question47           |
| hello_question48           |
| hello_question49           |
| hello_question5            |
| hello_question50           |
| hello_question51           |
| hello_question52           |
| hello_question53           |
| hello_question54           |
| hello_question55           |
| hello_question56           |
| hello_question57           |
| hello_question58           |
| hello_question59           |
| hello_question6            |
| hello_question60           |
| hello_question61           |
| hello_question62           |
| hello_question63           |
| hello_question64           |
| hello_question65           |
| hello_question66           |
| hello_question67           |
| hello_question68           |
| hello_question69           |
| hello_question7            |
| hello_question70           |
| hello_question71           |
| hello_question72           |
| hello_question73           |
| hello_question74           |
| hello_question75           |
| hello_question76           |
| hello_question77           |
| hello_question78           |
| hello_question79           |
| hello_question8            |
| hello_question80           |
| hello_question81           |
| hello_question82           |
| hello_question83           |
| hello_question84           |
| hello_question85           |
| hello_question86           |
| hello_question87           |
| hello_question88           |
| hello_question89           |
| hello_question9            |
| hello_question90           |
| hello_question91           |
| hello_question92           |
| hello_question93           |
| hello_question94           |
| hello_question95           |
| hello_question96           |
| hello_question97           |
| hello_question98           |
| hello_question99           |
+----------------------------+
```

## Benchmark

### master (rev-b1f88476db)

```
(venv) $ python manage.py bench_sql_flush 10
0th elapsed: 3.381
1th elapsed: 3.389
2th elapsed: 3.259
3th elapsed: 3.256
4th elapsed: 3.227
elapsed: 3.302 sec (+/- 0.07654421548104305)
(venv) $ python manage.py bench_sql_flush 100
0th elapsed: 3.318
1th elapsed: 3.341
2th elapsed: 3.282
3th elapsed: 3.278
4th elapsed: 3.394
elapsed: 3.323 sec (+/- 0.04785021314287499)
(venv) $ python manage.py bench_sql_flush 1000
0th elapsed: 3.575
1th elapsed: 3.509
2th elapsed: 3.761
3th elapsed: 3.533
4th elapsed: 3.504
elapsed: 3.577 sec (+/- 0.10670887280046382)
```

### ticket-31275 branch (rev-99d8419f7d)

with `reset_sequences=False`

```
(venv) $ python manage.py bench_sql_flush 10
0th elapsed: 0.546
1th elapsed: 0.502
2th elapsed: 0.524
3th elapsed: 0.515
4th elapsed: 0.498
elapsed: 0.517 sec (+/- 0.019)
(venv) $ python manage.py bench_sql_flush 100
0th elapsed: 0.560
1th elapsed: 0.567
2th elapsed: 0.596
3th elapsed: 0.547
4th elapsed: 0.607
elapsed: 0.575 sec (+/- 0.025)
(venv) $ python manage.py bench_sql_flush 1000
0th elapsed: 1.023
1th elapsed: 1.042
2th elapsed: 1.016
3th elapsed: 1.066
4th elapsed: 1.085
elapsed: 1.046 sec (+/- 0.029)
```

with `reset_sequences=True`

```
(venv) $ python manage.py bench_sql_flush 10 --reset-sequences
0th elapsed: 3.719
1th elapsed: 3.656
2th elapsed: 3.543
3th elapsed: 3.745
4th elapsed: 3.627
elapsed: 3.658 sec (+/- 0.080)
(venv) $ python manage.py bench_sql_flush 100 --reset-sequences
0th elapsed: 3.643
1th elapsed: 3.627
2th elapsed: 3.546
3th elapsed: 3.590
4th elapsed: 3.451
elapsed: 3.571 sec (+/- 0.077)
(venv) $ python manage.py bench_sql_flush 1000 --reset-sequences
0th elapsed: 3.799
1th elapsed: 3.704
2th elapsed: 3.816
3th elapsed: 3.846
4th elapsed: 3.902
elapsed: 3.813 sec (+/- 0.073)
```
