import os
import json
import requests
from requests_toolbelt import MultipartEncoder


access_token = '532a0328e01aa1509960111cb73f30be_3cdb6ea4c6e60805dd247f432afc7d1f'
appName = 'trending-bot'
postId = '11'

# 대상 서버 URL (이미지를 전송할 서버의 엔드포인트)
target_url = f'https://tistory.com/apis/post/attach?access_token={access_token}&blogName={appName}&postId={postId}&targetUr={appName}&output=json'

# 이미지가 있는 원본 URL
image_url = 'https://storage.googleapis.com/lsusports-com/2023/11/amt-1458200a301bf65316834603c5b401443748900a-546bfb12-listenlive-3.jpg'

image_extension = os.path.splitext(image_url)[-1].lower()

# 이미지 확장자에 따라 Content-Type 설정
if image_extension == '.jpg' or image_extension == '.jpeg':
    content_type = 'image/jpeg'
elif image_extension == '.png':
    content_type = 'image/png'
elif image_extension == '.gif':
    content_type = 'image/gif'
else:
    content_type = 'application/octet-stream'  # 기본값으로 설정

# MultipartEncoder를 사용하여 데이터 준비
multipart_data = MultipartEncoder(
    fields={
        'uploadedfile': ('image' + image_extension, requests.get(image_url).content, content_type)
    }
)

print(multipart_data.content_type)

# 요청 헤더 설정 (multipart/form-data로 전송)
headers = {
    'Content-Type': multipart_data.content_type,
    'Authorization': f'Bearer {access_token}'
}

# 파일을 대상 서버로 전송
response = requests.post(target_url, headers=headers, data=multipart_data)

thum_url = json.loads(response.text)['tistory']['url']

# 임시 파일 삭제
if response.status_code == 200:
    print('이미지 업로드 성공')
else:
    print('이미지 업로드 실패. 응답 코드:', response.status_code)



#asyncio.run(getTrendsToWrite(access_token))
