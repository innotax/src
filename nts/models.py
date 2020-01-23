from django.db import models
from django.urls import reverse


class CtaCert(models.Model):

    cert_nm = models.CharField(max_length=100, verbose_name='인증서명')
    pub_dt = models.DateField(verbose_name='유효기간시작일')
    end_dt = models.DateField(verbose_name='유효기간종료일')
    org_nm = models.CharField(max_length=20, verbose_name='인증기관')
    oid = models.CharField(max_length=30, verbose_name='인증기관ID')
    sn = models.CharField(max_length=20, verbose_name='시리얼넘버')
    file1 = models.CharField(max_length=1000, verbose_name='인증서')
    file2 = models.CharField(max_length=1000, verbose_name='개인키')
    cert_pw = models.CharField(max_length=20, verbose_name='인증서비번')
    num_used = models.IntegerField(default=0, verbose_name='선택횟수', null=True, blank=True)

    def __str__(self):
        return self.cert_nm

    def get_absolute_url(self):
        return reverse("nts:ctacert-detail", kwargs={"pk": self.pk})

    class Meta:
        unique_together = (('cert_nm', 'end_dt'),)

class CtaIdPw(models.Model):
    # id = models.AutoField(primary_key=True)
    # id = models.PositiveIntegerField(auto_created=True, unique=True)
    ctacert = models.ForeignKey(CtaCert, on_delete=models.CASCADE)
    ctaid = models.CharField(max_length=6, verbose_name='세무대리인 ID', primary_key=True)
    # ctaid = models.CharField(max_length=6, verbose_name='세무대리인 ID')
    pw = models.CharField(max_length=20, verbose_name='세무대리인 PW')
    num_used = models.IntegerField(default=0, verbose_name='선택횟수', null=True, blank=True)

    def __str__(self):
        return self.ctaid
    
    def get_absolute_url(self):
        return reverse("nts:ctaidpw_detail", kwargs={"pk": self.pk})

    class Meta:
        unique_together = (('ctacert', 'ctaid'),)
class BsIdPw(models.Model):
    # id = models.AutoField(primary_key=True)
    ctacert = models.ForeignKey(CtaCert, on_delete=models.CASCADE)
    ctaidpw = models.ForeignKey(CtaIdPw, on_delete=models.CASCADE)
    bsid = models.CharField(max_length=20, verbose_name='사용자 ID', primary_key=True)
    pw = models.CharField(max_length=20, verbose_name='사용자 PW')
    num_used = models.IntegerField( default=0, verbose_name='선택횟수', null=True, blank=True)

    def __str__(self):
        return self.bsid

    def get_absolute_url(self):
        return reverse("nts:bsidpw_detail", kwargs={"pk": self.pk})

    class Meta:
        unique_together = (('ctacert', 'ctaidpw', 'bsid'),)
    
    
