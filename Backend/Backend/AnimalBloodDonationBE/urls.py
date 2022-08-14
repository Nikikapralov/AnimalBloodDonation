from django.urls import path

from Backend.AnimalBloodDonationBE.views import GetAllOwnersAdmin, GetAllPetsAdmin, GetAllCases, \
    GetAllCurrentCaseImages, GetAllCasesAdmin, GetAllCommentsAdmin, GetAllCaseImagesAdmin, \
    GetAllPrivateMessageTablesAdmin, GetAllMessagesAdmin, GetAllCurrentCaseComments, GetSpecificCase

urlpatterns = [path("admin/owners/", GetAllOwnersAdmin.as_view(), name="owners_admin"),
               path("admin/pets/", GetAllPetsAdmin.as_view(), name="pets_admin"),
               path("admin/comments/", GetAllCommentsAdmin.as_view(), name="comments_admin"),
               path("admin/cases/", GetAllCasesAdmin.as_view(), name="cases_admin"),
               path("admin/case_images", GetAllCaseImagesAdmin.as_view(), name="case_images_admin"),
               path("admin/messages/", GetAllMessagesAdmin.as_view(), name="messages_admin"),
               path("admin/private_message_table/", GetAllPrivateMessageTablesAdmin.as_view(), name="private_message_table_admin"),


               path("cases/", GetAllCases.as_view(), name="cases"),
               path("cases/<int:pk>", GetSpecificCase.as_view(), name="case specific"),
               path("cases/<int:pk>/case_images/", GetAllCurrentCaseImages.as_view(), name="current case images"),
               path("cases/<int:pk>/comments/", GetAllCurrentCaseComments.as_view(), name="current case comments"),

               ]