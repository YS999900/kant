````markdown
# Git 명령어 치트시트

Git을 사용할 때 자주 사용하는 명령어를 기능별로 정리했다.

---

# 1. Git 기본 설정

## Git 버전 확인

```bash
git --version
```

## 사용자 이름 설정

```bash
git config --global user.name "이름"
```

## 사용자 이메일 설정

```bash
git config --global user.email "이메일"
```

## 전체 설정 확인

```bash
git config --global --list
```

## 특정 설정 삭제

```bash
git config --global --unset user.name
```

---

# 2. Git 저장소 시작

## 현재 폴더를 Git 저장소로 만들기

```bash
git init
```

현재 폴더에 `.git`이 생성되고 Git 버전 관리를 시작한다.

```text
일반 폴더
   ↓
git init
   ↓
Git 저장소
```

## 기존 Git 저장소 복제

```bash
git clone 저장소주소
```

예:

```bash
git clone https://github.com/user/project.git
```

원격 저장소의 파일뿐 아니라 Commit 기록과 Branch 정보까지 가져온다.

## Git 저장소 최상위 폴더 확인

```bash
git rev-parse --show-toplevel
```

---

# 3. 현재 상태 확인

## 파일 상태 확인

```bash
git status
```

대표적인 상태:

```text
U = Untracked
A = Added
M = Modified
D = Deleted
R = Renamed
```

## 아직 Stage하지 않은 변경내용 확인

```bash
git diff
```

## Stage된 변경내용 확인

```bash
git diff --staged
```

---

# 4. Staging Area

Git의 기본 흐름:

```text
Working Directory
      ↓
   git add
      ↓
Staging Area
      ↓
 git commit
      ↓
Repository
```

## 특정 파일 Stage

```bash
git add 파일명
```

예:

```bash
git add README.md
```

## 현재 폴더 기준 전체 Stage

```bash
git add .
```

현재 위치와 하위 폴더의 변경사항을 Stage한다.

## Git 저장소 전체 Stage

```bash
git add -A