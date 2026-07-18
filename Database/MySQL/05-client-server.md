# MySQL 클라이언트와 서버

## 오늘 공부한 내용

인터넷과 데이터베이스를 클라이언트/서버 구조로 이해했다.

인터넷에서는 클라이언트가 요청을 보내고, 서버가 요청에 대한 응답을 제공한다.

데이터베이스도 비슷하게 실제 데이터는 데이터베이스 서버에 저장되고, 데이터베이스 클라이언트가 명령을 보내면 서버가 그 명령에 따라 데이터를 제공한다.

## 데이터베이스 서버

데이터베이스 서버는 실제 데이터를 저장하고 관리하는 역할을 한다.

클라이언트가 SQL 명령을 보내면 데이터베이스 서버는 명령을 처리한 뒤 결과를 반환한다.

## 데이터베이스 클라이언트

데이터베이스 클라이언트는 데이터베이스 서버에 명령을 보내고 결과를 받아오는 도구이다.

내가 지금까지 터미널에서 사용한 `mysql` 명령어 기반 도구는 MySQL Monitor이며, 이것이 MySQL 클라이언트에 해당한다.

## MySQL Monitor

MySQL Monitor는 CLI(Command Line Interface) 기반 MySQL 클라이언트이다.

터미널에서 직접 SQL 명령어를 입력해 MySQL 서버와 통신한다.

```bash
cd /usr/local/mysql/bin
./mysql -uroot -p
```

## MySQL Workbench

MySQL Workbench도 MySQL 클라이언트이다.

MySQL Workbench는 GUI(Graphical User Interface)를 통해 데이터베이스를 더 쉽게 조작할 수 있는 도구이다.

테이블 조회, 쿼리 작성, 스키마 확인 등을 화면 기반으로 할 수 있다.

## CLI로 공부하는 이유

MySQL Workbench는 GUI로 쉽게 사용할 수 있지만, 당분간은 CLI 기반 MySQL Monitor로 공부하려고 한다.

CLI에서 직접 명령어를 입력하면 SQL 문법과 데이터베이스 동작 흐름을 더 명확하게 익힐 수 있다.

## 오늘 배운 점

MySQL 서버는 실제 데이터를 저장하고 관리하는 역할을 한다.

MySQL 클라이언트는 서버에 명령을 보내고 결과를 받아오는 역할을 한다.

MySQL Monitor와 MySQL Workbench는 모두 MySQL 서버에 접속해 명령을 보내는 클라이언트이다.

