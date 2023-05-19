import requests

def post_to_tistory(title, content, tags):
    # 티스토리 API 엔드포인트와 인증 정보 설정
    api_url = 'https://www.tistory.com/apis/post/write'
    access_token = 'YOUR_TISTORY_ACCESS_TOKEN'
    blog_name = 'YOUR_TISTORY_BLOG_NAME'

    # API 요청 데이터 설정
    data = {
        'access_token': access_token,
        'output': 'json',
        'blogName': blog_name,
        'title': title,
        'content': content,
        'category': '카테고리',
        'tag': ','.join(tags)
    }

    # API 요청 보내기
    response = requests.post(api_url, data=data)
    if response.status_code == 200:
        print('티스토리에 글이 성공적으로 작성되었습니다.')
    else:
        print('티스토리에 글 작성 실패:', response.text)


def post_to_blogger(title, content, labels):
    # Blogger API 엔드포인트와 인증 정보 설정
    api_url = 'https://www.googleapis.com/blogger/v3/blogs/BLOG_ID/posts'
    api_key = 'YOUR_BLOGGER_API_KEY'

    # API 요청 헤더 설정
    headers = {
        'Content-Type': 'application/json'
    }

    # API 요청 데이터 설정
    data = {
        'kind': 'blogger#post',
        'blog': {
            'id': 'BLOG_ID'
        },
        'title': title,
        'content': content,
        'labels': labels
    }

    # API 요청 보내기
    response = requests.post(api_url, headers=headers, json=data, params={'key': api_key})
    if response.status_code == 200:
        print('Blogger에 글이 성공적으로 작성되었습니다.')
    else:
        print('Blogger에 글 작성 실패:', response.text)


# 티스토리에 글 작성
post_to_tistory('티스토리 글 제목', '티스토리 글 내용', ['태그1', '태그2'])

# Blogger에 글 작성
post_to_blogger('Blogger 글 제목', 'Blogger 글 내용', ['라벨1', '라벨2'])
