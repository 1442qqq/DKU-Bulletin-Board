# DKU-Bulletin-Board
Bulletin Board Project for OSS work.

1.  웹사이트 주소는 다음과 같습니다: https://dku-bulletin-board.onrender.com
    무료 플랜이라 시간 제한이 있어서 평상시엔 로컬로 작업.


2.  Supabase DB 프로젝트 주소입니다: https://supabase.com/dashboard/project/[]
    프로젝트에 초대를 받아야 접속 가능.


3.  코드상에서 데이터베이스 참조하실 때는 아래 방식을 사용.
```
======================================================  
    from database import db #DB 객체 불러옴  
    from models import 테이블이름 #사용할 테이블 모델 불러옴  
======================================================  
```
    SQLAlchemy에 대해 제미나이를 갈구면 적당한 답이 나올 것  

    조회시: 모델명.query.all() 혹은 filter_by() 등 



4. views 디렉토리는 Flask 블루프린트를 저장하는 디렉토리.
```
======================================================  
from flask import render_template, Blueprint  
bp = Blueprint('적당한별명', __name__)  

@bp.route("주소")       # www.naver.com/news 같은 거 할떄 "/news" 같은 거  
def 실행할작업명():      # 사용자가 주소 접속시 실행  
    ...                 # 이런저런 작업들  
    return              # render_template("index.html")처럼 웹에 표시할 결과물  
======================================================  
```

5. templates 디렉토리는 html파일들을 담아두는 저장소. 


6. 로컬에서 테스트하려면 .env 파일에 DB주소를 적어야 함, 유출 위험으로 GitHub 업로드 금지.