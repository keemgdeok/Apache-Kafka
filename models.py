from django.db import models

class TblKafkaTest(models.Model):
    idx = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    col_a = models.CharField(max_length=50, blank=True, null=True)
    col_b = models.CharField(max_length=50, blank=True, null=True)
    col_c = models.CharField(max_length=50, blank=True, null=True)
    col_d = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "tbl_kafka_test"