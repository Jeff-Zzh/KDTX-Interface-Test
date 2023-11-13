import requests
import config

class ContractApi:
    def __init__(self):
        self.url_upload = config.BASE_URL + "/api/common/upload"
        self.url_add_contract = config.BASE_URL + "/api/contract"

    # 合同上传
    def upload_contract(self, token, file):
        return requests.post(url=self.url_upload,
                             files={"file":file}, # 形参有file，说明请求体request_body是多消息体数据Content-Type:multipart/form-data
                             headers={"Authorization":token})

    # 合同新增
    def add_contract(self, token, request_body):
        return requests.post(url=self.url_add_contract,
                             json=request_body,
                             headers={"Authorization":token})