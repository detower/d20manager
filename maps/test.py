# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'django_site'

class GeneralAbility(models.Model):
    id = models.IntegerField(primary_key=True)
    ruleset = models.ForeignKey('GeneralRuleset')
    name = models.CharField(max_length=100)
    short = models.CharField(max_length=5)
    class Meta:
        db_table = 'general_ability'

class GeneralBaseattackbonus(models.Model):
    id = models.IntegerField(primary_key=True)
    klass_level = models.ForeignKey('GeneralKlasslevel', unique=True)
    modifier = models.IntegerField()
    class Meta:
        db_table = 'general_baseattackbonus'

class GeneralCharability(models.Model):
    id = models.IntegerField(primary_key=True)
    ruleset = models.ForeignKey('GeneralRuleset')
    character = models.ForeignKey('GeneralCharacter')
    ability = models.ForeignKey(GeneralAbility)
    base_value = models.IntegerField()
    alter_value = models.IntegerField()
    class Meta:
        db_table = 'general_charability'

class GeneralCharacter(models.Model):
    id = models.IntegerField(primary_key=True)
    ruleset = models.ForeignKey('GeneralRuleset')
    name = models.CharField(max_length=255)
    alignment_lawfulness = models.FloatField()
    alignment_indole = models.FloatField()
    class Meta:
        db_table = 'general_character'

class GeneralCharklass(models.Model):
    id = models.IntegerField(primary_key=True)
    character = models.ForeignKey(GeneralCharacter)
    klass = models.ForeignKey('GeneralKlass')
    class Meta:
        db_table = 'general_charklass'

class GeneralCharskill(models.Model):
    id = models.IntegerField(primary_key=True)
    character = models.ForeignKey(GeneralCharacter)
    skill = models.ForeignKey('GeneralSkill')
    points = models.IntegerField()
    class Meta:
        db_table = 'general_charskill'

class GeneralFeat(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table = 'general_feat'

class GeneralFeatskill(models.Model):
    id = models.IntegerField(primary_key=True)
    feat = models.ForeignKey(GeneralFeat)
    skill = models.ForeignKey('GeneralSkill')
    modifier = models.IntegerField()
    class Meta:
        db_table = 'general_featskill'

class GeneralFortsave(models.Model):
    id = models.IntegerField(primary_key=True)
    klass_level = models.ForeignKey('GeneralKlasslevel', unique=True)
    modifier = models.IntegerField()
    class Meta:
        db_table = 'general_fortsave'

class GeneralKlass(models.Model):
    id = models.IntegerField(primary_key=True)
    ruleset = models.ForeignKey('GeneralRuleset')
    name = models.CharField(max_length=255)
    allowed_alignment_lawful_min = models.FloatField()
    allowed_alignment_lawful_max = models.FloatField()
    allowed_alignment_indole_min = models.FloatField()
    allowed_alignment_indole_max = models.FloatField()
    hit_die = models.CharField(max_length=50)
    class Meta:
        db_table = 'general_klass'

class GeneralKlasslevel(models.Model):
    id = models.IntegerField(primary_key=True)
    ruleset = models.ForeignKey('GeneralRuleset')
    klass = models.ForeignKey(GeneralKlass)
    level = models.IntegerField()
    class Meta:
        db_table = 'general_klasslevel'

class GeneralKlassskill(models.Model):
    id = models.IntegerField(primary_key=True)
    klass = models.ForeignKey(GeneralKlass)
    skill = models.ForeignKey('GeneralSkill')
    class Meta:
        db_table = 'general_klassskill'

class GeneralRefsave(models.Model):
    id = models.IntegerField(primary_key=True)
    klass_level = models.ForeignKey(GeneralKlasslevel, unique=True)
    modifier = models.IntegerField()
    class Meta:
        db_table = 'general_refsave'

class GeneralRuleset(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'general_ruleset'

class GeneralSkill(models.Model):
    id = models.IntegerField(primary_key=True)
    ruleset = models.ForeignKey(GeneralRuleset)
    name = models.CharField(max_length=100)
    ability = models.ForeignKey(GeneralAbility)
    trained_only = models.BooleanField()
    action = models.FloatField()
    try_again = models.BooleanField()
    ac_penalty = models.BooleanField()
    class Meta:
        db_table = 'general_skill'

class GeneralSkillsynergy(models.Model):
    id = models.IntegerField(primary_key=True)
    ruleset = models.ForeignKey(GeneralRuleset)
    activator = models.ForeignKey(GeneralSkill)
    activator_ranks = models.IntegerField()
    activated = models.ForeignKey(GeneralSkill)
    activated_modifier = models.IntegerField()
    class Meta:
        db_table = 'general_skillsynergy'

class GeneralSpecialfeat(models.Model):
    id = models.IntegerField(primary_key=True)
    klass_level = models.ForeignKey(GeneralKlasslevel)
    feat = models.ForeignKey(GeneralFeat, null=True, blank=True)
    class Meta:
        db_table = 'general_specialfeat'

class GeneralWillsave(models.Model):
    id = models.IntegerField(primary_key=True)
    klass_level = models.ForeignKey(GeneralKlasslevel, unique=True)
    modifier = models.IntegerField()
    class Meta:
        db_table = 'general_willsave'

class GeographyColumns(models.Model):
    f_table_catalog = models.TextField(blank=True) # This field type is a guess.
    f_table_schema = models.TextField(blank=True) # This field type is a guess.
    f_table_name = models.TextField(blank=True) # This field type is a guess.
    f_geography_column = models.TextField(blank=True) # This field type is a guess.
    coord_dimension = models.IntegerField(null=True, blank=True)
    srid = models.IntegerField(null=True, blank=True)
    type = models.TextField(blank=True)
    class Meta:
        db_table = 'geography_columns'

class GeometryColumns(models.Model):
    f_table_catalog = models.CharField(max_length=256, blank=True)
    f_table_schema = models.CharField(max_length=256, blank=True)
    f_table_name = models.CharField(max_length=256, blank=True)
    f_geometry_column = models.CharField(max_length=256, blank=True)
    coord_dimension = models.IntegerField(null=True, blank=True)
    srid = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'geometry_columns'

class Layer(models.Model):
    topology = models.ForeignKey('Topology')
    layer_id = models.IntegerField()
    schema_name = models.CharField(max_length=-1)
    table_name = models.CharField(max_length=-1)
    feature_column = models.CharField(max_length=-1)
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'layer'

class RacesCharrace(models.Model):
    id = models.IntegerField(primary_key=True)
    character = models.ForeignKey(GeneralCharacter, unique=True)
    race = models.ForeignKey('RacesRace')
    height = models.IntegerField()
    age = models.IntegerField()
    class Meta:
        db_table = 'races_charrace'

class RacesCulture(models.Model):
    id = models.IntegerField(primary_key=True)
    culture_type = models.IntegerField()
    culture_interaction_type = models.IntegerField()
    culture_form = models.IntegerField()
    class Meta:
        db_table = 'races_culture'

class RacesCultureform(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    class Meta:
        db_table = 'races_cultureform'

class RacesCultureinteractiontype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    class Meta:
        db_table = 'races_cultureinteractiontype'

class RacesCulturetype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    class Meta:
        db_table = 'races_culturetype'

class RacesKlasslanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    klass = models.ForeignKey(GeneralKlass)
    language = models.ForeignKey('RacesLanguage')
    class Meta:
        db_table = 'races_klasslanguage'

class RacesLanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    secret = models.BooleanField()
    class Meta:
        db_table = 'races_language'

class RacesRace(models.Model):
    id = models.IntegerField(primary_key=True)
    ruleset_id = models.IntegerField()
    name = models.TextField()
    mean_death_age = models.IntegerField()
    mean_height = models.IntegerField()
    speed = models.IntegerField()
    skill_points_modifier = models.IntegerField()
    level_adj = models.IntegerField()
    class Meta:
        db_table = 'races_race'

class RacesRaceability(models.Model):
    id = models.IntegerField(primary_key=True)
    race = models.ForeignKey(RacesRace)
    ability = models.ForeignKey(GeneralAbility)
    modifier = models.IntegerField()
    class Meta:
        db_table = 'races_raceability'

class RacesRacefeats(models.Model):
    id = models.IntegerField(primary_key=True)
    race = models.ForeignKey(RacesRace)
    feat = models.ForeignKey(GeneralFeat, null=True, blank=True)
    class Meta:
        db_table = 'races_racefeats'

class RacesRacelanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    race = models.ForeignKey(RacesRace)
    language = models.ForeignKey(RacesLanguage)
    class Meta:
        db_table = 'races_racelanguage'

class RacesRaceskills(models.Model):
    id = models.IntegerField(primary_key=True)
    race = models.ForeignKey(RacesRace)
    skill_id = models.IntegerField()
    modifier = models.IntegerField()
    class Meta:
        db_table = 'races_raceskills'

class RasterColumns(models.Model):
    r_table_catalog = models.TextField(blank=True) # This field type is a guess.
    r_table_schema = models.TextField(blank=True) # This field type is a guess.
    r_table_name = models.TextField(blank=True) # This field type is a guess.
    r_raster_column = models.TextField(blank=True) # This field type is a guess.
    srid = models.IntegerField(null=True, blank=True)
    scale_x = models.FloatField(null=True, blank=True)
    scale_y = models.FloatField(null=True, blank=True)
    blocksize_x = models.IntegerField(null=True, blank=True)
    blocksize_y = models.IntegerField(null=True, blank=True)
    same_alignment = models.BooleanField(null=True, blank=True)
    regular_blocking = models.BooleanField(null=True, blank=True)
    num_bands = models.IntegerField(null=True, blank=True)
    pixel_types = models.TextField(blank=True) # This field type is a guess.
    nodata_values = models.TextField(blank=True) # This field type is a guess.
    out_db = models.TextField(blank=True) # This field type is a guess.
    extent = models.GeometryField(null=True, blank=True)
    class Meta:
        db_table = 'raster_columns'

class RasterOverviews(models.Model):
    o_table_catalog = models.TextField(blank=True) # This field type is a guess.
    o_table_schema = models.TextField(blank=True) # This field type is a guess.
    o_table_name = models.TextField(blank=True) # This field type is a guess.
    o_raster_column = models.TextField(blank=True) # This field type is a guess.
    r_table_catalog = models.TextField(blank=True) # This field type is a guess.
    r_table_schema = models.TextField(blank=True) # This field type is a guess.
    r_table_name = models.TextField(blank=True) # This field type is a guess.
    r_raster_column = models.TextField(blank=True) # This field type is a guess.
    overview_factor = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'raster_overviews'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        db_table = 'south_migrationhistory'

class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True)
    auth_srid = models.IntegerField(null=True, blank=True)
    srtext = models.CharField(max_length=2048, blank=True)
    proj4text = models.CharField(max_length=2048, blank=True)
    class Meta:
        db_table = 'spatial_ref_sys'

class Topology(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=-1, unique=True)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()
    class Meta:
        db_table = 'topology'

