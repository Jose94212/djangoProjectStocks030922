from dataclasses import Field
from traceback import print_tb
from rest_framework import serializers
from app_platforms.models import ModelPlatforms

def is_negative(value):
    if value<0:
        raise serializers.ValidationError('Value must be positive')
    return value

class PlatformSerializer(serializers.ModelSerializer):  
    class Meta:
        model = ModelPlatforms
        fields = "__all__"

    def validate_pf_charges_account_open(self,value):
        if value<0:
            raise serializers.ValidationError("account opening charges cannot be negative")
        return value
    
    def validate_pf_charges_amc(self,value):
        if value<0:
            raise serializers.ValidationError("account maintenance charge cannot be negative")
        return value
    

    def validate(self, data):
        print("\ngoing to validate data")
        brokerages = ["pf_brokerage_equity_intraday1","pf_brokerage_equity_intraday2",
                    "pf_brokerage_equity_delivery1","pf_brokerage_equity_delivery2",
                    "pf_brokerage_fo","pf_brokerage_mf"]
        
        for brokerage in brokerages:
            print("\ngoing to validate:"+brokerage)
            if data.get(brokerage) and data.get(brokerage)<0:
                raise serializers.ValidationError("Brokerage %s cannot be negative" % brokerage)
        
        
        if data.get("pf_fd_rate") is True and data.get("pf_fd_rate")<=0:
            raise serializers.ValidationError("pf_fd_rate cannot be negative or 0")
        
        if data.get("pf_fd_rate") is False and isinstance(data.get("pf_fd_rate"),float):
            raise serializers.ValidationError("if pf_fd_rate is False, pf_fd_rate must be null")


        # if loan available, interest cannot be negative nor zero
        if data.get("pf_loans") is True and data.get("pf_loan_rate")<=0:
            raise serializers.ValidationError("pf_loan_rate cannot be negative or 0")
        
        print("\npf-loans",data.get("pf_loans"))
        if data.get("pf_loans") is False and isinstance(data.get("pf_loan_rate"),float):
            raise serializers.ValidationError("if pf_loans is False, pf_loan_rate must be null")
        

        
        return data