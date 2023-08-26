from rest_framework import routers

from .views import QuestionView, OptionView, AnswerView, UserView

router = routers.SimpleRouter()

router.register('questions', QuestionView)

router.register('options', OptionView)

router.register('answers', AnswerView)

router.register('users', UserView)

urlpatterns = router.urls