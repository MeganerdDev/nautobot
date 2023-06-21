"""Utilities for apps to integrate with and extend the existing Nautobot UI."""

from nautobot.core.apps import (
    HomePageItem,
    HomePagePanel,
    NavMenuAddButton,
    NavMenuGroup,
    NavMenuImportButton,
    NavMenuItem,
    NavMenuTab,
)
from nautobot.extras.choices import BannerClassChoices, ButtonColorChoices
from nautobot.extras.plugins import Banner
from nautobot.extras.plugins import TemplateExtension

__all__ = (
    "Banner",
    "BannerClassChoices",
    "ButtonColorChoices",
    "HomePageItem",
    "HomePagePanel",
    "NavMenuAddButton",
    "NavMenuGroup",
    "NavMenuImportButton",
    "NavMenuItem",
    "NavMenuTab",
    "TemplateExtension",
)
