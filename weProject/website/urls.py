from django.contrib import admin
from django.urls import path

from website.views import index, candidateLogin, candidateSignup, candidateIndex, candidateJobSearch, \
	candidateJobDescription, candidateProfile, candidateProfileDetails, candidateJobApplied, employerLogin, \
	employerSignup, employerIndex, employerProfile, employerProfileDetails, employerJobPost, employerNewJobPost, \
	employerJobCreated, employerCreatedJobs, employerCandidateApplied, employerAnalytics

urlpatterns = [
    path('admin/', admin.site.urls),
	path('',index),
	path('candidate-login',candidateLogin),
	path('candidate-signup',candidateSignup),
	path('candidate-index',candidateIndex),
	path('candidate-jobsearch',candidateJobSearch),
	path('candidate-jobdescription',candidateJobDescription),
	path('candidate-profile',candidateProfile),
	path('candidate-profiledetails',candidateProfileDetails),
	path('candidate-jobapplied',candidateJobApplied),
	path('employer-login',employerLogin),
	path('employer-signup',employerSignup),
	path('employer-index',employerIndex),
	path('employer-profile',employerProfile),
	path('employer-profiledetails',employerProfileDetails),
	path('employer-jobpost',employerJobPost),
	path('employer-newjobpost',employerNewJobPost),
	path('employer-jobcreated',employerJobCreated),
	path('employer-createdjobs',employerCreatedJobs),
	path('employer-candidate-applied',employerCandidateApplied),
	path('employer-analytics',employerAnalytics)
]