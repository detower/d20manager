from django.contrib import admin

from .models import *


class RuleSetAdmin(admin.ModelAdmin):
    pass
admin.site.register(RuleSet, RuleSetAdmin)

class FeatAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feat, FeatAdmin)

class KlassLevelAdmin(admin.ModelAdmin):
    pass
admin.site.register(KlassLevel, KlassLevelAdmin)

class BaseAttackBonusAdmin(admin.ModelAdmin):
    pass
admin.site.register(BaseAttackBonus, BaseAttackBonusAdmin)

class FortSaveAdmin(admin.ModelAdmin):
    pass
admin.site.register(FortSave, FortSaveAdmin)

class FeatSkillAdmin(admin.ModelAdmin):
    pass
admin.site.register(FeatSkill, FeatSkillAdmin)

class RefSaveAdmin(admin.ModelAdmin):
    pass
admin.site.register(RefSave, RefSaveAdmin)

class WillSaveAdmin(admin.ModelAdmin):
    pass
admin.site.register(WillSave, WillSaveAdmin)

class SpecialFeatAdmin(admin.ModelAdmin):
    pass
admin.site.register(SpecialFeat, SpecialFeatAdmin)

class AbilityAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ability, AbilityAdmin)

class SkillAdmin(admin.ModelAdmin):
    pass
admin.site.register(Skill, SkillAdmin)

class SkillSynergyAdmin(admin.ModelAdmin):
    pass
admin.site.register(SkillSynergy, SkillSynergyAdmin)

class KlassAdmin(admin.ModelAdmin):
    pass
admin.site.register(Klass, KlassAdmin)

class CharKlassAdmin(admin.ModelAdmin):
    pass
admin.site.register(CharKlass, CharKlassAdmin)

class KlassSkillAdmin(admin.ModelAdmin):
    pass
admin.site.register(KlassSkill, KlassSkillAdmin)

class CharacterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Character, CharacterAdmin)

class CharAbilityAdmin(admin.ModelAdmin):
    pass
admin.site.register(CharAbility, CharAbilityAdmin)

class CharSkillAdmin(admin.ModelAdmin):
    pass
admin.site.register(CharSkill, CharSkillAdmin)
