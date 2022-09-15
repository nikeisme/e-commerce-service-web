# 💡 e-commerce-service-web
- Fruitte 스토어 Backend 데이터베이스 및 API 개발

# 📚 목차
[1.요구사항 분석](#1-요구사항-분석)<br>
[2.기술 스택](#이동할-위치)<br>
[3.My Chellenge](#이동할-위치)<br>
[4.ERD](#이동할-위치)<br>
[5.API 명세서](#이동할-위치)<br>
[6.기능 구현 gif ](#이동할-위치)<br>
[7.Todo ](#이동할-위치)<br>

# ✏️1. 요구사항 분석
<details markdown="1">
<summary>기능구현을 위한 DB생성</summary>
- 회원/상품/결제/주문 DB 생성
</details>
<details markdown="2">
<summary>정보 입력,수정 시 데이터 형식 유효성 검사</summary>
</details>
<details markdown="3">
<summary>REST API에서 벗어난 Param 또는 요청 오류에 대한 응답처리</summary>
</details>
<details markdown="4">
<summary>유저를 이용자,관리자로 나누어 포지션별로 권한 부여</summary>
- 이용자는 회원가입,결제,주문을 제외하고 조회 권한만 허용 <br>
- 관리자는 모든 권한 부여
</details>

# 🔋 2. 기술 스택
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white">  

# 🔥 3.My Chellenge

-  dj-rest-auth로 회원관리 도전
-  drf authentication permission 적재적소에 적용하기 도전

# 🔖 4.ERD
  
  ![image](https://user-images.githubusercontent.com/99165573/190404182-9667f9a3-c912-424a-9bf6-f1650ac2a9ee.png)
  
# 📝 5. API 명세서

![image](https://user-images.githubusercontent.com/99165573/190404517-330f836d-b08e-4eda-9fc2-fbd7629f487e.png)
![image](https://user-images.githubusercontent.com/99165573/190404648-4d509945-8697-441d-82f9-0b1f1fb404f5.png)
![image](https://user-images.githubusercontent.com/99165573/190404745-d077fa69-1769-4633-ac59-5726bc359963.png)
![image](https://user-images.githubusercontent.com/99165573/190404817-bf1e3770-82ef-4de5-88d4-80e05c98e1b0.png)


# 🚀6. 기능 구현

## 회원 관리 
  - 회원 가입 시, username,password,is_staff(관리자 여부)에 대한 정보를 기입<br>
    user는 이용자로, staff는 관리자로 계정을 생성
    
    ![register-staff](https://user-images.githubusercontent.com/99165573/190355263-da185c58-54c9-42cf-9c89-421b038ede1f.gif)

  - 회원 가입 시, 아이디, eamil 중복 데이터 유효성 검사
    데이터가 중복될 시, 입력이 불가합니다.
  
    ![register-유효성검사](https://user-images.githubusercontent.com/99165573/190355534-4d6b5b0a-faf3-4770-9b33-2db83a08958b.gif)

  - 로그인 시, key가 발급됨.
  
    ![Login-staff](https://user-images.githubusercontent.com/99165573/190355909-f6f45d9c-1c86-4af2-8168-6e60b99af322.gif)
    
  - 로그아웃
  
    ![Logout-–-staff](https://user-images.githubusercontent.com/99165573/190356077-9282970c-7202-4c95-9646-6de324e59616.gif)

## 상품 관리

  - 관리자 즉, is_staff 값이 1(True)인 계정은  상품 등록,조회,수정,삭제 가능
    
    ![product-등록-staff](https://user-images.githubusercontent.com/99165573/190378426-8a1c59fd-9384-4975-84ab-146745234b35.gif)
    ![prodcut-수정-업데이트-staff](https://user-images.githubusercontent.com/99165573/190378571-b4356635-359c-4342-beed-296e4f12f86d.gif)

  - 이용자 즉, is_straff 값이 0(False)인 계정은 상품 목록 조회만 가능 / 등록,수정,삭제는 불가
    
    ![image](https://user-images.githubusercontent.com/99165573/190379729-e7451270-c5b6-4132-9f4a-b6688b265882.png)

  ## 주문 관리
  
  - 이용자는 Address(주소), Recipient(받는사람),User(사용자 이름),Product(구매할 상품) 을 입력
   
  ![image](https://user-images.githubusercontent.com/99165573/190394239-b6200951-38b7-4126-8dff-67b13de8912e.png)

  - 관리자는 주문에 대한 수정, 삭제 가능
    
  ![image](https://user-images.githubusercontent.com/99165573/190393290-8ccfa1a4-9474-47d2-86df-f2f13d94d72a.png)

  ## 결제 관리
  
   - 이용자는 Payments Method(결제 방법)과 Orders(주문) 을 입력
    
   ![image](https://user-images.githubusercontent.com/99165573/190393673-0a4dc6aa-47ba-47c9-8422-98c0772cc7c8.png)

   - 관리자는 결제에 대한 수정 삭제 가능
      
   ![image](https://user-images.githubusercontent.com/99165573/190393773-3f133bb4-9d82-46c1-8efc-a0ab7934a636.png)

# ❤️‍🔥 7. 리팩토링할 때 할 것

- 장바구니 모델 추가
- 각 테이블 구체적인 컬럼 추가
- 주문/ 결제에 관한 UPDATE, DELETE 고도화 (ex 주문 취소 시, 주문 정보와 주문자가 동일하지 않으면 오류 응답 처리)

     
    

