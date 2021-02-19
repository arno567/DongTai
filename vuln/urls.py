#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# datetime:2021/1/25 下午7:01
# software: PyCharm
# project: lingzhi-engine

from django.urls import path

from vuln.views.method_pool import MethodPoolEndPoint
from vuln.views.search import SearchEndPoint
from vuln.views.signer import RunSigner
from vuln.views.strategy_run import StrategyRunEndPoint
from vuln.views.vul_rule import VulRuleEndPoint
from vuln.views.vul_rule_detail import VulRuleDetailEndPoint
from vuln.views.vul_rule_save import VulRuleSaveEndPoint

urlpatterns = [
    # todo
    #   策略保存
    #   结果详情
    path('search', SearchEndPoint.as_view()),
    path('rule', VulRuleEndPoint.as_view()),
    path('rule/detail', VulRuleDetailEndPoint.as_view()),
    path('rule/save', VulRuleSaveEndPoint.as_view()),
    path('run', StrategyRunEndPoint.as_view()),
    path('method_pools', MethodPoolEndPoint.as_view()),
    path('sign', RunSigner.as_view()),
]
