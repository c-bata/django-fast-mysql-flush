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

### master (rev-f344c75fb0)

```
(venv) $ python manage.py bench_sql_flush 10
0th elapsed: 3.376
1th elapsed: 4.016
2th elapsed: 4.212
3th elapsed: 3.992
4th elapsed: 3.869
elapsed: 3.893 sec (+/- 0.31413987647226255)
(venv) $ python manage.py bench_sql_flush 100
0th elapsed: 3.757
1th elapsed: 3.474
2th elapsed: 4.844
3th elapsed: 3.800
4th elapsed: 3.569
elapsed: 3.889 sec (+/- 0.5504522162602504)
(venv) $ python manage.py bench_sql_flush 1000
0th elapsed: 4.293
1th elapsed: 3.920
2th elapsed: 3.622
3th elapsed: 3.700
4th elapsed: 4.023
elapsed: 3.912 sec (+/- 0.2674345091622726)
```

### ticket-31275 branch (rev-8c65f9f856)

with `reset_sequences=False`

```
$ python manage.py bench_sql_flush 10
0th elapsed: 0.669
1th elapsed: 0.534
2th elapsed: 0.518
3th elapsed: 0.493
4th elapsed: 0.463
elapsed: 0.535 sec (+/- 0.0797195768792136)
(venv) $ python manage.py bench_sql_flush 100
0th elapsed: 0.607
1th elapsed: 0.555
2th elapsed: 0.542
3th elapsed: 0.572
4th elapsed: 0.622
elapsed: 0.580 sec (+/- 0.03411013544312636)
(venv) $ python manage.py bench_sql_flush 1000
0th elapsed: 1.198
1th elapsed: 1.123
2th elapsed: 1.136
3th elapsed: 1.128
4th elapsed: 1.073
elapsed: 1.132 sec (+/- 0.044564402281665624)
```

with `reset_sequences=True`

```
(venv) $ python manage.py bench_sql_flush 10 --reset-sequences
0th elapsed: 1.912
1th elapsed: 1.785
2th elapsed: 1.733
3th elapsed: 1.729
4th elapsed: 1.650
elapsed: 1.762 sec (+/- 0.09680283421863593)
(venv) $ python manage.py bench_sql_flush 100 --reset-sequences
0th elapsed: 1.812
1th elapsed: 1.786
2th elapsed: 1.784
3th elapsed: 1.848
4th elapsed: 1.859
elapsed: 1.818 sec (+/- 0.03468588048962085)
(venv) $ python manage.py bench_sql_flush 1000 --reset-sequences
0th elapsed: 2.363
1th elapsed: 2.430
2th elapsed: 2.482
3th elapsed: 2.556
4th elapsed: 2.493
elapsed: 2.465 sec (+/- 0.07246214754639008)
```
