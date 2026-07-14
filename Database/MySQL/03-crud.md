# MySQL CRUD

## 오늘 공부한 내용

생활코딩 MySQL 강의에서 CRUD를 공부하고 직접 실습했다.

CRUD는 데이터를 다루는 기본 기능을 의미한다.

- Create: 데이터 추가
- Read: 데이터 조회
- Update: 데이터 수정
- Delete: 데이터 삭제

## CRUD의 중요도

Create와 Read는 대부분의 서비스에서 필수적으로 사용된다.

Update와 Delete는 서비스 도메인에 따라 있을 수도 있고 없을 수도 있다.

## Create

Create는 데이터를 추가하는 기능이다.

```sql
INSERT INTO 테이블명 (컬럼1, 컬럼2)
VALUES (데이터1, 데이터2);
```

## Read

Read는 데이터를 조회하는 기능이다.

```sql
SELECT 컬럼명
FROM 테이블명;
```

전체 컬럼을 조회할 때는 `*`를 사용할 수 있다.

```sql
SELECT *
FROM 테이블명;
```

조건을 걸어 조회할 때는 `WHERE`를 사용한다.

```sql
SELECT *
FROM 테이블명
WHERE 조건;
```

정렬할 때는 `ORDER BY`를 사용하고, 조회 개수를 제한할 때는 `LIMIT`을 사용할 수 있다.

```sql
SELECT *
FROM 테이블명
ORDER BY 컬럼명 DESC
LIMIT 10;
```

## Update

Update는 기존 데이터를 수정하는 기능이다.

```sql
UPDATE 테이블명
SET 컬럼명 = '수정사항'
WHERE 조건;
```

`WHERE` 조건을 작성하지 않으면 해당 컬럼의 모든 데이터가 수정될 수 있으므로 주의해야 한다.

## Delete

Delete는 데이터를 삭제하는 기능이다.

```sql
DELETE FROM 테이블명
WHERE 조건;
```

`DELETE`도 `WHERE` 조건을 작성하지 않으면 테이블의 모든 데이터가 삭제될 수 있으므로 주의해야 한다.
