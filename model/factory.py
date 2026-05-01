from abc import ABC, abstractmethod
from typing import Optional
from langchain_core.embeddings import Embeddings
# from langchain_community.chat_models import BaseChatModel
# from langchain_community.embeddings import DashScopeEmbeddings
# from langchain_community.chat_models.tongyi import ChatTongyi
from utils.config_handler import rag_conf
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import os
import dotenv
dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY_FREE0")
OPENAI_API_BASE = os.getenv("OPENAI_BASE_URL0_FOR_PROXY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
API_BASE = os.getenv("BASE_PROXY")
os.environ["HTTP_PROXY"] = API_BASE
os.environ["HTTPS_PROXY"] = API_BASE
# llm = ChatOpenAI(
#     model="gpt-3.5-turbo",
#     api_key=OPENAI_API_KEY,
#     base_url=OPENAI_API_BASE,
#     temperature=0
# )
# embeddings = OpenAIEmbeddings(
#     model="text-embedding-3-small",
#     api_key=OPENAI_API_KEY,
#     base_url=OPENAI_API_BASE
# )


class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self) -> Optional[Embeddings]:
        pass


class ChatModelFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings]:
        # return ChatTongyi(model=rag_conf["chat_model_name"])
        # return ChatGoogleGenerativeAI(
        #     # model="gemini-2.5-pro",GEMINI_API_KEY  "models/text-embedding-004",API_BASE
        #     model=rag_conf["chat_model_name"],
        #     api_key=GEMINI_API_KEY,
        #     # google_base_url=API_BASE
        # )
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            api_key=OPENAI_API_KEY,
            base_url=OPENAI_API_BASE,
            temperature=0
        )


class EmbeddingsFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings]:
        # return DashScopeEmbeddings(model=rag_conf["embedding_model_name"])
        # return GoogleGenerativeAIEmbeddings(
        #     model=rag_conf["embedding_model_name"],  # ✅ 使用支持 embedding 的模型
        #     google_api_key=GEMINI_API_KEY,  # ✅ 提供 API Key
        #     # google_base_url=API_BASE  # ✅ 提供 API Base URL
        # )
        return OpenAIEmbeddings(
            model="text-embedding-3-small",
            api_key=OPENAI_API_KEY,
            base_url=OPENAI_API_BASE
        )


chat_model = ChatModelFactory().generator()
embed_model = EmbeddingsFactory().generator()
