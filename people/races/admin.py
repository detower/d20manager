from django.contrib import admin

from .models import *


class LanguageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Language, LanguageAdmin)

class KlassLanguageAdmin(admin.ModelAdmin):
    pass
admin.site.register(KlassLanguage, KlassLanguageAdmin)

class RaceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Race, RaceAdmin)

class CharRaceAdmin(admin.ModelAdmin):
    pass
admin.site.register(CharRace, CharRaceAdmin)

class RaceLanguageAdmin(admin.ModelAdmin):
    pass
admin.site.register(RaceLanguage, RaceLanguageAdmin)

class RaceAbilityAdmin(admin.ModelAdmin):
    pass
admin.site.register(RaceAbility, RaceAbilityAdmin)

class RaceFeatsAdmin(admin.ModelAdmin):
    pass
admin.site.register(RaceFeats, RaceFeatsAdmin)

class RaceSkillsAdmin(admin.ModelAdmin):
    pass
admin.site.register(RaceSkills, RaceSkillsAdmin)
