from django.contrib import admin
from django.core.urlresolvers import NoReverseMatch
from django.utils.translation import ugettext_lazy as _

from gstudio.admin.forms import IntersectionAdminForm
import reversion
from gstudio.settings import GSTUDIO_VERSIONING
if GSTUDIO_VERSIONING == True:
    parent_class = reversion.VersionAdmin
else:
    parent_class = admin.ModelAdmin 

class IntersectionAdmin(parent_class):
    pass
