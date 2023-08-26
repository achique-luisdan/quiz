from rest_framework import routers

from .views import QuestionView, OptionView, AnswerView

router = routers.SimpleRouter()

router.register('questions', QuestionView)

router.register('options', OptionView)

router.register('answers', AnswerView)

urlpatterns = router.urls