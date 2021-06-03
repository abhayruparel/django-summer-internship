from django.urls import path
from . import views


urlpatterns = [
    # path('', views.jobForm),
    path('jobApplication/', views.oldForm),
    path('showApplicants/', views.showApplications),
    path('editApplication/<int:id>', views.editApplication),
    path('updateApplication/<int:id>', views.updateApplication),
    path('deleteApplication/<int:id>', views.deleteApplication),
    path('test/', views.test)
]
