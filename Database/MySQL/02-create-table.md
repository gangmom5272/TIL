# CREATE TABLE

## 오늘 한 공부

MySQL에서 `CREATE TABLE`을 사용해 테이블을 생성하는 방법을 공부했다.

## 실습 SQL

```sql
CREATE TABLE topic (
    id INT(11) NOT NULL AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT NULL,
    created DATETIME NOT NULL,
    author VARCHAR(30) NULL,
    profile VARCHAR(100) NULL,
    PRIMARY KEY (id)
);
```

## 컬럼 정리

- `id`: 각 행을 구분하기 위한 고유 번호
- `title`: 제목
- `description`: 본문 내용
- `created`: 작성 시간
- `author`: 작성자
- `profile`: 작성자 소개

## 문법 정리

- `INT`: 정수 타입
- `VARCHAR(n)`: 최대 n자까지 저장할 수 있는 문자열 타입
- `TEXT`: 긴 문자열을 저장할 수 있는 타입
- `DATETIME`: 날짜와 시간을 저장하는 타입
- `NOT NULL`: 반드시 값이 있어야 함
- `NULL`: 값이 없어도 됨
- `AUTO_INCREMENT`: 값이 자동으로 증가함
- `PRIMARY KEY`: 각 행을 고유하게 식별하는 기본키


