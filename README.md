# π‘ e-commerce-service-web
- Fruitte μ€ν μ΄ Backend λ°μ΄ν°λ² μ΄μ€ λ° API κ°λ°

# π λͺ©μ°¨
<h3>1.μκ΅¬μ¬ν­λΆμ<br>
<h3>2.κΈ°μ μ€ν<br>
<h3>3.MyChallenge<br>
<h3>4.ERD<br>
<h3>5.APIλͺμΈμ<br>
<h3>6.κΈ°λ₯ κ΅¬ν<br>
<h3>7.λ¦¬ν©ν λ§ν  λ ν  κ²

# βοΈ1. μκ΅¬μ¬ν­ λΆμ
<details markdown="1">
<summary>κΈ°λ₯κ΅¬νμ μν DBμμ±</summary>
- νμ/μν/κ²°μ /μ£Όλ¬Έ DB μμ±
</details>
<details markdown="2">
<summary>μ λ³΄ μλ ₯,μμ  μ λ°μ΄ν° νμ μ ν¨μ± κ²μ¬</summary>
</details>
<details markdown="3">
<summary>REST APIμμ λ²μ΄λ Param λλ μμ²­ μ€λ₯μ λν μλ΅μ²λ¦¬</summary>
</details>
<details markdown="4">
<summary>μ μ λ₯Ό μ΄μ©μ,κ΄λ¦¬μλ‘ λλμ΄ ν¬μ§μλ³λ‘ κΆν λΆμ¬</summary>
- μ΄μ©μλ νμκ°μ,κ²°μ ,μ£Όλ¬Έμ μ μΈνκ³  μ‘°ν κΆνλ§ νμ© <br>
- κ΄λ¦¬μλ λͺ¨λ  κΆν λΆμ¬
</details>

# π 2. κΈ°μ  μ€ν
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white">  

# π₯ 3.My Challenge

-  dj-rest-authλ‘ νμκ΄λ¦¬ λμ 
-  drf authentication permission μ μ¬μ μμ μ μ©νκΈ° λμ 

# π 4.ERD
  
  ![image](https://user-images.githubusercontent.com/99165573/190404182-9667f9a3-c912-424a-9bf6-f1650ac2a9ee.png)
  
# π 5. API λͺμΈμ

![image](https://user-images.githubusercontent.com/99165573/190404517-330f836d-b08e-4eda-9fc2-fbd7629f487e.png)
![image](https://user-images.githubusercontent.com/99165573/190404648-4d509945-8697-441d-82f9-0b1f1fb404f5.png)
![image](https://user-images.githubusercontent.com/99165573/190404745-d077fa69-1769-4633-ac59-5726bc359963.png)
![image](https://user-images.githubusercontent.com/99165573/190404817-bf1e3770-82ef-4de5-88d4-80e05c98e1b0.png)


# π6. κΈ°λ₯ κ΅¬ν

## νμ κ΄λ¦¬ 
  - νμ κ°μ μ, username,password,is_staff(κ΄λ¦¬μ μ¬λΆ)μ λν μ λ³΄λ₯Ό κΈ°μ<br>
    userλ μ΄μ©μλ‘, staffλ κ΄λ¦¬μλ‘ κ³μ μ μμ±
    
    ![register-staff](https://user-images.githubusercontent.com/99165573/190355263-da185c58-54c9-42cf-9c89-421b038ede1f.gif)

  - νμ κ°μ μ, μμ΄λ, eamil μ€λ³΅ λ°μ΄ν° μ ν¨μ± κ²μ¬
    λ°μ΄ν°κ° μ€λ³΅λ  μ, μλ ₯μ΄ λΆκ°ν©λλ€.
  
    ![register-μ ν¨μ±κ²μ¬](https://user-images.githubusercontent.com/99165573/190355534-4d6b5b0a-faf3-4770-9b33-2db83a08958b.gif)

  - λ‘κ·ΈμΈ μ, keyκ° λ°κΈλ¨.
  
    ![Login-staff](https://user-images.githubusercontent.com/99165573/190355909-f6f45d9c-1c86-4af2-8168-6e60b99af322.gif)
    
  - λ‘κ·Έμμ
  
    ![Logout-β-staff](https://user-images.githubusercontent.com/99165573/190356077-9282970c-7202-4c95-9646-6de324e59616.gif)

## μν κ΄λ¦¬

  - κ΄λ¦¬μ μ¦, is_staff κ°μ΄ 1(True)μΈ κ³μ μ  μν λ±λ‘,μ‘°ν,μμ ,μ­μ  κ°λ₯
    
    ![product-λ±λ‘-staff](https://user-images.githubusercontent.com/99165573/190378426-8a1c59fd-9384-4975-84ab-146745234b35.gif)
    ![prodcut-μμ -μλ°μ΄νΈ-staff](https://user-images.githubusercontent.com/99165573/190378571-b4356635-359c-4342-beed-296e4f12f86d.gif)

  - μ΄μ©μ μ¦, is_straff κ°μ΄ 0(False)μΈ κ³μ μ μν λͺ©λ‘ μ‘°νλ§ κ°λ₯ / λ±λ‘,μμ ,μ­μ λ λΆκ°
    
    ![image](https://user-images.githubusercontent.com/99165573/190379729-e7451270-c5b6-4132-9f4a-b6688b265882.png)

  ## μ£Όλ¬Έ κ΄λ¦¬
  
  - μ΄μ©μλ Address(μ£Όμ), Recipient(λ°λμ¬λ),User(μ¬μ©μ μ΄λ¦),Product(κ΅¬λ§€ν  μν) μ μλ ₯
   
  ![image](https://user-images.githubusercontent.com/99165573/190394239-b6200951-38b7-4126-8dff-67b13de8912e.png)

  - κ΄λ¦¬μλ μ£Όλ¬Έμ λν μμ , μ­μ  κ°λ₯
    
  ![image](https://user-images.githubusercontent.com/99165573/190393290-8ccfa1a4-9474-47d2-86df-f2f13d94d72a.png)

  ## κ²°μ  κ΄λ¦¬
  
   - μ΄μ©μλ Payments Method(κ²°μ  λ°©λ²)κ³Ό Orders(μ£Όλ¬Έ) μ μλ ₯
    
   ![image](https://user-images.githubusercontent.com/99165573/190393673-0a4dc6aa-47ba-47c9-8422-98c0772cc7c8.png)

   - κ΄λ¦¬μλ κ²°μ μ λν μμ  μ­μ  κ°λ₯
      
   ![image](https://user-images.githubusercontent.com/99165573/190393773-3f133bb4-9d82-46c1-8efc-a0ab7934a636.png)

# β€οΈβπ₯ 7. λ¦¬ν©ν λ§ν  λ ν  κ²

- μ₯λ°κ΅¬λ λͺ¨λΈ μΆκ°
- κ° νμ΄λΈ κ΅¬μ²΄μ μΈ μ»¬λΌ μΆκ°
- μ£Όλ¬Έ/ κ²°μ μ κ΄ν UPDATE, DELETE κ³ λν (ex μ£Όλ¬Έ μ·¨μ μ, μ£Όλ¬Έ μ λ³΄μ μ£Όλ¬Έμκ° λμΌνμ§ μμΌλ©΄ μ€λ₯ μλ΅ μ²λ¦¬)

     
    

