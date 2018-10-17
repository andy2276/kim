[아이디어]
1.로딩 스테이트를 만들어서 스텍의 1에는 무조건 이것을 넣을것
	-임포트만 하면 그 객체는 살아 있고, 그 안에서 일어난 것들은 모두 기록이 되기때문에 로딩스테이트가
	있으면 그것만 받아주면 global로 남겨야하는 것들은 모두 살아 있을것이다. 그러면 언제든 자료를 쓰기
	편할것이다.
아군 클래스클래스
	class clPlayerBody:
		mvX-맴버변수 x 바디의 x위치 추가로 벡터좌표 mvVX와 mvVY를 만들어서 이동좌표를 만들자
		mvY-멤버변수 y 바디의 y위치
<<<<<<< HEAD
		위에꺼는 절대 좌표를 받는 친구고 벡터좌표도 만들어서 간단하게 계산하자
		mvVX,mvVY - 멤버변수 벡터 좌표 - 아래로 간다면 현재좌표에서 +(-mvVY를 해주면 된다)
=======
		현 mvx,mvy에다가 mvVx를 더하는 방식으로 하면 더 간단하게 계산이 될것이다.
>>>>>>> 0d045d0357603cfffdaa18594645f15851c72e77
		mvHp-멤버변수 hp
		mvSpeed-멤버변수 speed
		mvBodyImage - 멤버변수 bodyimage
		mvRotatedImage - 멤버 변수 rotated bodyimage
		mvRotate - 멤버변수 rotate
	멤버함수
		update
		draw
[알림]
1.gameframe work는 무조건 gf로 as임포트해서 받을것
2.교수님의 수정된 gameframe work를 쓸것
3.로고 이후에 무조건 로딩스테이트를 들어갈 것
4.시작은 무조건 main스테이트고 그다음 로고 스테이트고 그다음 로딩 스테이트로 진입
[추가]
1.https://m.blog.naver.com/samsjang/220498694383 openCV공부
2.rotate 함수 구현
3.타임 모듈 추가하여 프레임관련된 것을 timeToDeltaTime으로 만들기
