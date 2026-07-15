````markdown
# MySQL JOIN

## 오늘 공부한 내용

오늘 MySQL에서는 관계형 데이터베이스의 필요성과 `JOIN`을 공부했다.

데이터베이스 개론에서 공부한 정규화, 외래키, 테이블 분리 개념과 MySQL 실습 내용이 연결되었다.

## 관계형 데이터베이스가 필요한 이유

관계형 데이터베이스는 중복된 데이터를 줄이고, 관련 있는 데이터를 여러 테이블로 나누어 관리하기 위해 사용한다.

중복 데이터를 제거하기 위해 정규화를 수행하고, 나누어진 테이블을 연결할 때 외래키를 사용한다.

예를 들어 `topic` 테이블에는 글 정보가 있고, `author` 테이블에는 작성자 정보가 있을 수 있다.

이때 `topic.author_id`가 `author.id`를 참조하면 두 테이블을 관계로 연결할 수 있다.

## 테이블 분리의 트레이드 오프

테이블을 나누는 것은 장점과 단점이 모두 있다.

테이블을 나누지 않으면 하나의 테이블에서 모든 데이터를 한눈에 볼 수 있다.

하지만 같은 작성자 정보가 여러 행에 반복되어 데이터 중복이 발생할 수 있다.

반대로 테이블을 나누면 중복을 줄일 수 있지만, 데이터를 볼 때 여러 테이블을 함께 확인해야 하는 불편함이 생긴다.

이때 `JOIN`을 사용하면 나누어진 테이블을 다시 연결해서 한눈에 조회할 수 있다.

## JOIN

`JOIN`은 두 개 이상의 테이블을 연결해서 데이터를 조회할 때 사용한다.

오늘은 `topic` 테이블과 `author` 테이블을 `author_id`와 `id` 기준으로 연결했다.

## LEFT JOIN

`LEFT JOIN`은 왼쪽 테이블의 데이터를 기준으로 오른쪽 테이블을 연결한다.

```sql
SELECT *
FROM topic
LEFT JOIN author
ON topic.author_id = author.id;
```

위 쿼리는 `topic` 테이블의 `author_id`와 `author` 테이블의 `id`가 같은 데이터를 연결한다.

## 실습 결과

```text
+----+------------+-------------------+---------------------+-----------+------+--------+---------------------------+
| id | title      | description       | created             | author_id | id   | name   | profile                   |
+----+------------+-------------------+---------------------+-----------+------+--------+---------------------------+
|  1 | MySQL      | MySQL is...       | 2018-01-01 12:10:11 |         1 |    1 | egoing | developer                 |
|  2 | Oracle     | Oracle is ...     | 2018-01-03 13:01:10 |         1 |    1 | egoing | developer                 |
|  3 | SQL Server | SQL Server is ... | 2018-01-20 11:01:10 |         2 |    2 | duru   | database administrator    |
|  4 | PostgreSQL | PostgreSQL is ... | 2018-01-23 01:03:03 |         3 |    3 | taeho  | data scientist, developer |
|  5 | MongoDB    | MongoDB is ...    | 2018-01-30 12:31:03 |         1 |    1 | egoing | developer                 |
+----+------------+-------------------+---------------------+-----------+------+--------+---------------------------+
```

`SELECT *`을 사용하면 두 테이블의 모든 컬럼이 출력된다.

이 경우 `topic.id`와 `author.id`처럼 같은 이름의 컬럼이 함께 출력되어 결과가 복잡해질 수 있다.

## 테이블 별칭 사용

테이블에 별칭을 붙이면 쿼리를 더 짧고 읽기 쉽게 작성할 수 있다.

```sql
SELECT
    t.id,
    t.title,
    t.description,
    t.created,
    a.name,
    a.profile
FROM topic t
LEFT JOIN author a
ON t.author_id = a.id;
```

위 쿼리에서 `topic`은 `t`, `author`는 `a`라는 별칭으로 사용했다.

## 필요한 컬럼만 조회하기

`SELECT *` 대신 필요한 컬럼만 지정하면 결과를 더 깔끔하게 볼 수 있다.

```sql
SELECT
    t.id,
    t.title,
    t.description,
    t.created,
    a.name,
    a.profile
FROM topic t
LEFT JOIN author a
ON t.author_id = a.id;
```

## 실습 결과

```text
+----+------------+-------------------+---------------------+--------+---------------------------+
| id | title      | description       | created             | name   | profile                   |
+----+------------+-------------------+---------------------+--------+---------------------------+
|  1 | MySQL      | MySQL is...       | 2018-01-01 12:10:11 | egoing | developer                 |
|  2 | Oracle     | Oracle is ...     | 2018-01-03 13:01:10 | egoing | developer                 |
|  3 | SQL Server | SQL Server is ... | 2018-01-20 11:01:10 | duru   | database administrator    |
|  4 | PostgreSQL | PostgreSQL is ... | 2018-01-23 01:03:03 | taeho  | data scientist, developer |
|  5 | MongoDB    | MongoDB is ...    | 2018-01-30 12:31:03 | egoing | developer                 |
+----+------------+-------------------+---------------------+--------+---------------------------+
```

## DB 개론과 연결

DB 개론에서 정규화는 중복을 줄이기 위해 테이블을 나누는 과정이라고 배웠다.

MySQL 실습에서는 나누어진 `topic` 테이블과 `author` 테이블을 `JOIN`으로 다시 연결해 조회했다.

즉, 정규화로 테이블을 나누고, 외래키와 `JOIN`을 통해 필요한 데이터를 다시 합쳐서 볼 수 있다.

## 오늘 배운 점

관계형 데이터베이스는 중복을 줄이기 위해 데이터를 여러 테이블로 나누어 관리한다.

테이블을 나누면 중복은 줄어들지만 데이터를 한눈에 보기 어려워질 수 있다.

이 문제를 해결하기 위해 `JOIN`을 사용한다.

`JOIN`을 사용할 때는 테이블 별칭을 활용하고, `SELECT *`보다 필요한 컬럼만 선택하는 것이 결과를 이해하기 쉽다.
````