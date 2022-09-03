from datetime import datetime
from email.policy import default
from django.db import models

# Create your models here.


class ModelPlatforms(models.Model):
    pf_name = models.CharField(max_length=255, blank=False)
    pf_id = models.AutoField(primary_key=True)

    pf_equity=models.BooleanField(default=True,editable=True)
    pf_forex=models.BooleanField(default=False,editable=True)
    pf_commodities=models.BooleanField(default=False,editable=True)
    pf_mutualfunds = models.BooleanField(default=False,editable=True)

    pf_international_markets= models.BooleanField(default=False,editable=True)
    pf_india_market= models.BooleanField(default=True,editable=True)

    pf_equity_intraday = models.BooleanField(default=False,editable=True)
    pf_equity_delivery = models.BooleanField(default=False,editable=True)
    pf_gtt_order = models.BooleanField(default=False,editable=True)
    pf_future_options = models.BooleanField(default=True,editable=True)

    pf_own_chart = models.BooleanField(default=True,editable=True)
    pf_thirdparty_chart_available = models.BooleanField(default=False,editable=True)
    pf_thirdparty_charts= models.CharField(max_length=255, editable=True, blank=True,default='')

    pf_loans= models.BooleanField(default=False, editable=True)
    pf_fixed_deposits   = models.BooleanField(default=False, editable=True)

    pf_loan_rate=models.FloatField(editable=True, blank=True, null=True)
    pf_fd_rate=models.FloatField(editable=True, blank=True, null=True)

    pf_gold_bonds = models.BooleanField(default=False,editable=True)
    pf_ipo = models.BooleanField(default=True,editable=True)

    pf_charges_account_open = models.IntegerField(blank=True,editable=True,default=1000)
    pf_charges_amc  = models.IntegerField(blank=True,editable=True,default=1000)
    pf_brokerage_equity_intraday1 = models.IntegerField(blank=True,editable=True,default=20)
    pf_brokerage_equity_intraday2 = models.FloatField(blank=True,editable=True,default=0.5)     
    pf_brokerage_equity_delivery1= models.IntegerField(blank=True,editable=True,default=20)
    pf_brokerage_equity_delivery2= models.FloatField(blank=True,editable=True,default=0.5)
    pf_brokerage_fo=models.FloatField(blank=True, editable=True,default=1000)
    pf_brokerage_mf = models.FloatField(blank=True, editable=True,default=1000)
    
    pf_create_date = models.DateField(auto_now_add=True,null=True)
    pf_last_update = models.DateField(auto_now=True,null=True)


    # def save(self, *args, **kwargs):
    #     if self.pf_active and self.pf_market_active==False:
    #         self.pf_active = False
    #     if self.pf_market_active ==False:
    #         self.pf_active = False
        
    #     super(ModelPlatforms, self).save(*args, **kwargs)
            

