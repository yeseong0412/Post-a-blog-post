import requests

def post_to_tistory(title, content, tags):
    # 티스토리 API 엔드포인트와 인증 정보 설정
    api_url = 'https://www.tistory.com/apis/post/write'
    access_token = 'YOUR_TISTORY_ACCESS_TOKEN'  # 티스토리 액세스 토큰을 여기에 입력하세요
    blog_name = 'YOUR_TISTORY_BLOG_NAME'  # 티스토리 블로그 이름을 여기에 입력하세요

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

    try:
        # API 요청 보내기
        response = requests.post(api_url, data=data)
        response.raise_for_status()

        if response.status_code == 200: #200은 정상작동 됬다는 뜻
            print('티스토리에 글이 성공적으로 작성되었습니다.')
        else:
            print('티스토리에 글 작성 실패:', response.text)
    except requests.exceptions.RequestException as e:
        print('티스토리 API 요청 에러:', e)
    except requests.exceptions.HTTPError as e:
        print('HTTP 에러 발생:', e)
    except requests.exceptions.ConnectionError as e:
        print('네트워크 연결 오류:', e)
    except requests.exceptions.Timeout as e:
        print('요청 시간 초과:', e)
    except requests.exceptions.TooManyRedirects as e:
        print('너무 많은 리다이렉션 발생:', e)
    except Exception as e:
        print('예외가 발생했습니다:', e)


def post_to_blogger(title, content, labels):
    # Blogger API 엔드포인트와 인증 정보 설정
    api_url = 'https://www.googleapis.com/blogger/v3/blogs/BLOG_ID/posts'
    api_key = 'YOUR_BLOGGER_API_KEY'  # Blogger API 키를 여기에 입력하세요

    # API 요청 헤더 설정
    headers = {
        'Content-Type': 'application/json'
    }

    # API 요청 데이터 설정
    data = {
        'kind': 'blogger#post',
        'blog': {
            'id': 'BLOG_ID'  # 블로그 ID를 여기에 입력하세요
        },
        'title': title,
        'content': content,
        'labels': labels
    }

    try:
        # API 요청 보내기
        response = requests.post(api_url, headers=headers, json=data, params={'key': api_key})
        response.raise_for_status()

        if response.status_code == 200:
            print('Blogger에 글이 성공적으로 작성되었습니다.')
        else:
            print('Blogger에 글 작성 실패:', response.text)
    except requests.exceptions.RequestException as e:
        print('Blogger API 요청 에러:', e)
    except requests.exceptions.HTTPError as e:
        print('HTTP 에러 발생:', e)
    except requests.exceptions.ConnectionError as e:
        print('네트워크 연결 오류:', e)
    except requests.exceptions.Timeout as e:
        print('요청 시간 초과:', e)
    except requests.exceptions.TooManyRedirects as e:
        print('너무 많은 리다이렉션 발생:', e)
    except Exception as e:
        print('예외가 발생했습니다:', e)


# 티스토리에 글 작성
post_to_tistory('티스토리 글 제목', '티스토리 글 내용', ['태그1', '태그2'])

# Blogger에 글 작성
post_to_blogger('Blogger 글 제목', 'Blogger 글 내용', ['라벨1', '라벨2'])
