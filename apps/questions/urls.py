from rest_framework import routers

from .views import TopicView, QuestionView, OptionView, AnswerView, UserView

router = routers.SimpleRouter()

router.register('topics', TopicView)

router.register('questions', QuestionView)

router.register('options', OptionView)

router.register('answers', AnswerView)

router.register('users', UserView)

urlpatterns = router.urls