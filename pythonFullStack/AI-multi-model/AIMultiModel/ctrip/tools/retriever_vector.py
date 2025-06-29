'''本代码基于向量检索的智能FAQ系统，用于查询航空公司的政策信息'''

import re  #用于正则表达式处理，分割FAQ文档
import numpy as np  #用于向量计算和相似度排序
from langchain_community.embeddings import ZhipuAIEmbeddings  #智谱 AI 的嵌入模型，用于将文本转换为向量。
from langchain_core.tools import tool  #Langchain的工具装饰器，将函数转化为可被智能代理调用的工具
from langchain_openai import OpenAIEmbeddings

# 读取 FAQ 文本文件。
faq_text = None
with open('../order_faq.md', encoding='utf8') as f:
    faq_text = f.read()
# 将 FAQ 文本按标题分割成多个文档，每个文档都是一个字典
docs = [{"page_content": txt} for txt in re.split(r"(?=\n##)", faq_text)]
#初始化文本嵌入模型，将文本转化为向量表示
embeddings_model = ZhipuAIEmbeddings(
    model="embedding-3",
    api_key="18b5dee69df74c2ea63edd094fff9f3e.htyjBc465bSe64t5",
)

# embeddings_model = OpenAIEmbeddings(
#     model="text-embedding-3-small",
#     api_key="sk-ZKECakqu96gnIMx1iBsKkhHNl0qX3VnIDOJdtxPzTcFZdD1u",
#     base_url="https://xiaoai.plus/v1"
# )


# 定义向量存储检索器类
#定义向量存储检查器类
class VectorStoreRetriever:
    def __init__(self, docs: list, vectors: list):  #初始化文档列表和对应的向量列表
        # 存储文档和对应的向量
        self._arr = np.array(vectors)
        self._docs = docs

    @classmethod
    def from_docs(cls, docs):  #类方法，从文档列表生成向量，并创建检索器实例
        # 从文档生成嵌入向量
        embeddings = embeddings_model.embed_documents([doc["page_content"] for doc in docs])
        vectors = embeddings
        return cls(docs, vectors)

    def query(self, query: str, k: int = 5) -> list[dict]:
        # 对查询生成嵌入向量
        embed = embeddings_model.embed_query(query)
        # 计算查询向量与文档向量的相似度
        scores = np.array(embed) @ self._arr.T
        # 获取相似度最高的 k 个文档的索引
        top_k_idx = np.argpartition(scores, -k)[-k:]
        top_k_idx_sorted = top_k_idx[np.argsort(-scores[top_k_idx])]
        # 返回相似度最高的 k 个文档及其相似度
        #相似度的计算使用点积，这在向量维度归一化后等价于余弦相似度
        return [
            {**self._docs[idx], "similarity": scores[idx]} for idx in top_k_idx_sorted
        ]


# 创建向量存储检索器实例
retriever = VectorStoreRetriever.from_docs(docs)


# 定义工具函数，用于查询航空公司的政策
@tool
def lookup_policy(query: str) -> str:
    """查询公司政策，检查某些选项是否允许。
    在进行航班变更或其他'写'操作之前使用此函数。"""
    # 查询相似度最高的 k 个文档
    docs = retriever.query(query, k=2)
    # 返回这些文档的内容
    return "\n\n".join([doc["page_content"] for doc in docs])


if __name__ == '__main__':  # 测试代码
    print(lookup_policy('怎么才能退票呢？'))
