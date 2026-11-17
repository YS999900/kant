# Git 명령어 치트시트

> Git 명령어를 기능별로 빠르게 찾아보기 위한 정리

---

## 1. Git 기본 설정

| 명령어 | 기능 | 설명 |
|---|---|---|
| `git --version` | Git 버전 확인 | 설치된 Git 버전 확인 |
| `git config --global user.name "이름"` | 사용자 이름 설정 | Commit 작성자 이름 |
| `git config --global user.email "이메일"` | 이메일 설정 | Commit 작성자 이메일 |
| `git config --global --list` | 전체 설정 확인 | 현재 Global 설정 확인 |
| `git config --global --unset user.name` | 설정 삭제 | 등록된 이름 삭제 |

### 핵심

```text
config = Git 환경설정
--global = 이 컴퓨터의 Git 전체에 적용
```

---

## 2. Git 저장소

| 명령어 | 기능 | 설명 |
|---|---|---|
| `git init` | Git 저장소 생성 | 현재 폴더에서 Git 관리 시작 |
| `git clone 주소` | 저장소 복제 | 원격 Git 저장소를 로컬로 복제 |
| `git rev-parse --show-toplevel` | 저장소 Root 확인 | `.git`이 있는 최상위 폴더 확인 |

### 차이

| 명령어 | 언제 사용? |
|---|---|
| `git init` | 내가 새 프로젝트를 시작할 때 |
| `git clone` | 이미 존재하는 GitHub 프로젝트를 가져올 때 |

---

## 3. 현재 상태 확인

| 명령어 | 기능 |
|---|---|
| `git status` | 파일들의 현재 Git 상태 확인 |
| `git diff` | 아직 Stage하지 않은 변경내용 확인 |
| `git diff --staged` | Stage된 변경내용 확인 |

### VS Code Git 상태 표시

| 표시 | 의미 |
|---|---|
| `U` | Untracked - 아직 Git이 추적하지 않음 |
| `A` | Added - Stage에 추가됨 |
| `M` | Modified - 수정됨 |
| `D` | Deleted - 삭제됨 |
| `R` | Renamed - 이름 변경됨 |

---

## 4. Stage

| 명령어 | 기능 |
|---|---|
| `git add 파일명` | 특정 파일 Stage |
| `git add .` | 현재 위치와 하위 경로의 변경사항 Stage |
| `git add -A` | Git 저장소 전체 변경사항 Stage |
| `git restore --staged 파일명` | Stage 취소 |

### `git add .` vs `git add -A`

| 명령어 | 범위 |
|---|---|
| `git add .` | 현재 위치 기준 |
| `git add -A` | Git 저장소 전체 |

### 흐름

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

---

## 5. Commit

| 명령어 | 기능 |
|---|---|
| `git commit -m "메시지"` | Commit 생성 + 메시지 작성 |
| `git commit` | 편집기를 열어 Commit 메시지 작성 |

예:

```bash
git commit -m "docs: update Git notes"
```

구조:

| 부분 | 의미 |
|---|---|
| `git commit` | Commit 생성 |
| `-m` | Message를 직접 지정 |
| `"docs: update Git notes"` | Commit 메시지 |

---

## 6. Commit Convention

| Type | 의미 | 예 |
|---|---|---|
| `feat` | 새로운 기능 | `feat: add login` |
| `fix` | 버그 수정 | `fix: resolve login error` |
| `docs` | 문서 수정 | `docs: update README` |
| `style` | 코드 스타일 수정 | `style: fix indentation` |
| `refactor` | 코드 구조 개선 | `refactor: login logic` |
| `test` | 테스트 코드 | `test: add login test` |
| `chore` | 설정 및 기타 작업 | `chore: update package` |

### WIP

```text
WIP = Work In Progress
```

아직 작업 중이라는 의미.

예:

```bash
git commit -m "docs: update Git notes (WIP)"
```

---

## 7. Commit 기록 확인

| 명령어 | 기능 |
|---|---|
| `git log` | Commit 기록 자세히 확인 |
| `git log --oneline` | Commit을 한 줄씩 확인 |
| `git log --oneline --all` | 모든 Branch의 Commit 확인 |
| `git log --oneline --all --graph` | Branch 흐름을 그래프로 확인 |
| `git log --oneline --all --graph --decorate` | Branch 이름까지 함께 표시 |
| `git show` | 최근 Commit 내용 확인 |
| `git show 커밋ID` | 특정 Commit 확인 |

예:

```text
* 34abc12 (feature/login) feat: add login
| * 91abc25 (main) docs: update README
|/
* a12bc34 initial commit
```

---

## 8. Branch

| 명령어 | 기능 |
|---|---|
| `git branch` | Branch 목록 확인 |
| `git branch --list` | Branch 목록 확인 |
| `git branch 브랜치명` | Branch 생성 |
| `git switch 브랜치명` | Branch 이동 |
| `git checkout 브랜치명` | Branch 이동 - 기존 방식 |
| `git switch -c 브랜치명` | Branch 생성 + 이동 |
| `git checkout -b 브랜치명` | Branch 생성 + 이동 - 기존 방식 |

### 추천 방식

| 작업 | 추천 명령어 |
|---|---|
| Branch 생성 | `git branch feature/login` |
| Branch 이동 | `git switch feature/login` |
| 생성 + 이동 | `git switch -c feature/login` |

```text
-c = create
```

---

## 9. Branch 삭제 및 이름 변경

| 명령어 | 기능 |
|---|---|
| `git branch -d 브랜치명` | Branch 안전하게 삭제 |
| `git branch --delete 브랜치명` | Branch 안전하게 삭제 |
| `git branch -D 브랜치명` | Branch 강제 삭제 |
| `git branch -M main` | 현재 Branch 이름을 main으로 강제 변경 |

### 차이

| 옵션 | 의미 |
|---|---|
| `-d` | 안전하게 삭제 |
| `-D` | 강제 삭제 |
| `-M` | Branch 이름 강제 변경 |

---

## 10. Merge

| 명령어 | 기능 |
|---|---|
| `git merge 브랜치명` | 지정한 Branch를 현재 Branch에 병합 |

예:

```bash
git switch main
git merge feature/login
```

의미:

```text
feature/login
      ↓
     main
```

### 중요

```text
git merge 가져올브랜치

현재 Branch ← 가져올 Branch
```

---

## 11. Merge Conflict

두 Branch에서 **같은 파일의 같은 부분을 다르게 수정**하면 Conflict가 발생할 수 있다.

### 해결 순서

| 순서 | 작업 |
|---|---|
| 1 | 충돌난 파일 확인 |
| 2 | 사용할 코드 선택 및 수정 |
| 3 | 파일 저장 |
| 4 | `git add .` |
| 5 | Commit |
| 6 | Push |

예:

```bash
git add .
git commit -m "merge: resolve conflict"
git push
```

---

## 12. Remote

| 명령어 | 기능 |
|---|---|
| `git remote` | Remote 이름 확인 |
| `git remote -v` | Remote 이름 + 주소 확인 |
| `git remote add origin 주소` | Remote 등록 |
| `git remote remove origin` | Remote 삭제 |
| `git remote set-url origin 주소` | Remote 주소 변경 |

### Remote 이름

```text
origin
backup
company
github
```

등 원하는 이름을 사용할 수 있다.

예:

```bash
git remote add origin GitHub주소
git remote add backup GitLab주소
```

---

## 13. Push / Pull / Fetch

| 명령어 | 기능 |
|---|---|
| `git push -u origin main` | 처음 원격 저장소에 Push |
| `git push` | Commit을 원격 저장소에 업로드 |
| `git pull` | 원격 변경사항 가져오기 + 현재 Branch에 반영 |
| `git fetch` | 원격 변경사항을 가져오기만 함 |

### Pull vs Fetch

| 명령어 | 의미 |
|---|---|
| `git fetch` | 가져오기만 함 |
| `git pull` | 가져오기 + 반영 |

---

## 14. Local / Remote 상태

예:

```text
c009a72 (HEAD -> main) docs: update TIL
c310a46 (origin/main) feat: add gitignore
```

| 표시 | 의미 |
|---|---|
| `HEAD` | 내가 현재 작업 중인 위치 |
| `main` | 로컬 main Branch |
| `origin` | 원격 저장소의 별명 |
| `origin/main` | 로컬이 알고 있는 원격 main 위치 |

### Local이 한 Commit 앞선 경우

```text
A → B → C
    ↑   ↑
origin/main
        HEAD → main
```

Push 후:

```text
A → B → C
        ↑
HEAD → main
origin/main
```

로그에서는:

```text
c009a72 (HEAD -> main, origin/main)
```

처럼 표시될 수 있다.

---

## 15. HEAD

| 용어 | 의미 |
|---|---|
| `HEAD` | 현재 내가 작업하고 있는 위치 |
| `main` | Branch 이름 |
| Commit | 프로젝트의 특정 저장 시점 |
| Hash | Commit의 고유 ID |

구조:

```text
HEAD
 ↓
main
 ↓
Commit C
```

---

## 16. Reset

| 명령어 | Commit | Stage | Working Directory | 쉽게 |
|---|---|---|---|---|
| `git reset --soft ID` | 이동 | 유지 | 유지 | 다시 Commit할래 |
| `git reset --mixed ID` | 이동 | 해제 | 유지 | 다시 수정할래 |
| `git reset --hard ID` | 이동 | 해제 | 되돌림 | 작업도 버릴래 |

### Soft

```bash
git reset --soft 커밋ID
```

Commit만 취소하고 Stage는 유지.

### Mixed

```bash
git reset --mixed 커밋ID
```

또는:

```bash
git reset 커밋ID
```

Commit + Stage를 취소하고 파일 수정내용은 유지.

### Hard

```bash
git reset --hard 커밋ID
```

Commit + Stage + 파일 수정내용까지 되돌림.

> `--hard`는 작업 내용이 사라질 수 있으므로 주의.

---

## 17. Reflog

| 명령어 | 기능 |
|---|---|
| `git reflog` | HEAD 등의 이동 기록 확인 |
| `git reset --hard HEAD@{1}` | 이전 HEAD 위치로 이동 |

예:

```text
abc123 HEAD@{0}: reset
def456 HEAD@{1}: commit
ghi789 HEAD@{2}: commit
```

### 주의

```text
git reflog
→ Git의 HEAD 이동 기록

history
→ 터미널에서 입력한 명령어 기록
```

---

## 18. 파일 복원 및 삭제

| 명령어 | 기능 |
|---|---|
| `git restore 파일명` | 수정내용 되돌리기 |
| `git restore --staged 파일명` | Stage 취소 |
| `git rm 파일명` | 파일 삭제 + Git에 반영 |
| `git rm --cached 파일명` | 파일은 남기고 Git 추적만 중단 |
| `git mv 기존명 새이름` | 파일 이름 변경 |

예:

```bash
git mv 28 28.md
```

VS Code에서:

```text
R = Renamed
```

로 표시될 수 있다.

---

## 19. .gitignore

Git이 추적하지 않을 파일을 지정한다.

### 생성

```bash
touch .gitignore
```

### 예

```gitignore
*.dat
*.log
.env
node_modules/
```

| 패턴 | 의미 |
|---|---|
| `*.dat` | 모든 `.dat` 파일 제외 |
| `*.log` | 모든 로그 파일 제외 |
| `.env` | 환경설정 파일 제외 |
| `node_modules/` | 해당 폴더 제외 |

주로:

```text
개인정보
API Key
환경설정
로그
임시 파일
빌드 파일
```

등을 제외한다.

---

## 20. 과거 Commit 이동

| 명령어 | 기능 |
|---|---|
| `git checkout 커밋ID` | 특정 Commit으로 이동 |
| `git switch --detach 커밋ID` | 특정 Commit으로 이동 |
| `git switch main` | 다시 main으로 돌아오기 |

특정 Commit으로 직접 이동하면:

```text
detached HEAD
```

상태가 될 수 있다.

---

# Git 전체 작업 흐름

| 단계 | 명령어 | 의미 |
|---|---|---|
| 1 | 파일 수정 | 실제 코드 작업 |
| 2 | `git status` | 현재 상태 확인 |
| 3 | `git diff` | 수정내용 확인 |
| 4 | `git add .` | Stage |
| 5 | `git diff --staged` | Commit될 내용 확인 |
| 6 | `git commit -m "메시지"` | 버전 기록 |
| 7 | `git push` | GitHub 업로드 |

```text
Working Directory
        ↓
     git add
        ↓
  Staging Area
        ↓
   git commit
        ↓
Local Repository
        ↓
     git push
        ↓
GitHub Repository
```

---

# Branch 작업 흐름

| 단계 | 명령어 |
|---|---|
| Branch 생성 + 이동 | `git switch -c feature/login` |
| 파일 작업 | 코드 수정 |
| Stage | `git add .` |
| Commit | `git commit -m "feat: add login"` |
| main 이동 | `git switch main` |
| Merge | `git merge feature/login` |
| GitHub 업로드 | `git push` |

---

# 협업 기본 흐름

| 상황 | 작업 |
|---|---|
| Repository 처음 받음 | `git clone 주소` |
| 작업 전 최신 내용 반영 | `git pull` |
| 작업 내용 Stage | `git add .` |
| Commit | `git commit -m "메시지"` |
| GitHub 업로드 | `git push` |
| 다른 사람이 먼저 Push함 | `git pull` 후 다시 `git push` |
| Conflict 발생 | 충돌 해결 → add → commit → push |

---

# ⭐ 가장 자주 사용하는 명령어

| 명령어 | 이것만 기억 |
|---|---|
| `git init` | Git 관리 시작 |
| `git clone 주소` | 저장소 복제 |
| `git status` | 현재 상태 |
| `git diff` | 뭐가 바뀌었나 |
| `git add .` | Stage |
| `git commit -m "메시지"` | 버전 기록 |
| `git log --oneline` | Commit 기록 |
| `git branch` | Branch 확인 |
| `git switch -c 브랜치명` | Branch 생성 + 이동 |
| `git switch main` | main 이동 |
| `git merge 브랜치명` | Branch 병합 |
| `git remote -v` | 원격 주소 확인 |
| `git pull` | 원격 변경 가져오기 |
| `git push` | GitHub 업로드 |

---

# 핵심 암기

```text
init    = 시작
status  = 상태
diff    = 차이
add     = Stage
commit  = 기록
log     = 기록 보기
branch  = 작업 가지
switch  = Branch 이동
merge   = 병합
remote  = 원격 저장소
pull    = 받아오기
push    = 올리기
reset   = 되돌리기
reflog  = HEAD 이동 기록
clone   = 저장소 복제
```

> **Git 기본:** `수정 → add → commit → push`  
> **Branch 작업:** `branch → 작업 → commit → main → merge → push`