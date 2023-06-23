"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls"), name="accounts"),
    path("api/transaction/", include("transaction.urls"), name="transaction"),
    path("api/banks/", include("banks.urls"), name="banks"),
]
