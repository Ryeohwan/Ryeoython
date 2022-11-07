# 구해줘 홈즈 11조

## 멤버

- 이예은
- 안려환

## 메인화면

| 제목            | 내용                                                                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 메인페이지 html | [WebContent/index.html](https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/blob/main/WebContent/index.html) |
| 메인 js         | [WebContent/js/my.js](https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/blob/main/WebContent/js/my.js)     |
| 회원가입 js     | [WebContent/js/join.js](https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/blob/main/WebContent/js/join.js) |

- 메인 화면  
  <img src="https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/raw/main/img/%EB%A9%94%EC%9D%B8%ED%99%94%EB%A9%B4.PNG">

## 구현화면

| 구현 내용                             | code                                                                                                                                                                       |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| memberDao                             | [src/member/dao/MemberDao.java](https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/blob/main/src/member/dao/MemberDao.java)                 |
| member(dto)                           | [src/member/dto/Member.java](https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/blob/main/src/member/dto/Member.java)                       |
| SecVO(dto)                            | [src/member/dto/SecVO.java](https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/blob/main/src/member/dto/SecVO.java)                         |
| methods                               | [src/member/service/MemberService.java](https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/blob/main/src/member/service/MemberService.java) |
| main html (메인,로그인 포함)          | [WebContent/index.html](https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/blob/main/WebContent/index.html)                                 |
| memberInsertForm html (회원가입 화면) | [WebContent/memberInsertForm.html](https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/blob/main/WebContent/memberInsertForm.html)           |

- 로그인 기능

<img src="https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/raw/main/img/%EB%A1%9C%EA%B7%B8%EC%9D%B8%EC%84%B1%EA%B3%B5.PNG">

- 회원가입 기능

<img src="https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/raw/main/img/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.PNG">

- 회원 중복체크

<img src="https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/raw/main/img/%ED%9A%8C%EC%9B%90%EC%A4%91%EB%B3%B5%EC%B2%B4%ED%81%AC.PNG">

- 회원 가입 성공

<img src="https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/raw/main/img/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%EC%84%B1%EA%B3%B5.PNG">

- 암호화 되어 저장된 pw (sha-26)와 name(aes) 값

<img src="https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/raw/main/img/salt_db.PNG">

<img src="https://lab.ssafy.com/s08/a19/10_whereismyhome_algo/pair11_ahnryeohwan_leeyeeun/-/raw/main/img/%EC%95%94%ED%98%B8%ED%99%94.PNG">

```
public int addMember(Member memberModel) {
		if ( memberDao.selectMember(memberModel.getId()) != null ) {
			return 1;
		} else {
		           try {
		        	   byte[] key=OpenCrypt.generateKey("AES",128);
		        	   System.out.println("key length:"+key.length);
		        	   SecVO sec=
new SecVO(memberModel.getId(),UUID.randomUUID().toString(),OpenCrypt.byteArrayToHex(key));
		        	   memberDao.insertSecurity(sec);
		        	   memberModel.setName(OpenCrypt.aesEncrypt(memberModel.getName(), key));
		        	   String pw = OpenCrypt.byteArrayToHex(OpenCrypt.getSHA256(memberModel.getPw(), sec.getSalt()));
		               memberModel.setPw(pw);
		               memberDao.insertMember(memberModel);
		                   return 3;
		           }catch(Exception e ){
		        	  e.printStackTrace();
			               return 2;
		           }
		}
	}
```

sha-256 알고리즘으로 암호화된 pw 값의 길이가 너무 길기 때문에
저장할 땐 byte array 값을 Hex로 바꿔서 db에 저장을 해주었습니다.

`String pw = OpenCrypt.byteArrayToHex(OpenCrypt.getSHA256(memberModel.getPw(), sec.getSalt())); memberModel.setPw(pw); `
