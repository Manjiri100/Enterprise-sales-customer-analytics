import argparse, csv, random
from pathlib import Path
from datetime import date, timedelta

SEED=42
random.seed(SEED)

def d():
    return (date(2024,1,1)+timedelta(days=random.randint(0,730))).isoformat()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",default="data/generated")
    ap.add_argument("--scale-factor",type=float,default=1.0)
    a=ap.parse_args()
    out=Path(a.output); out.mkdir(parents=True,exist_ok=True)
    n={ "customers":max(100,int(100_000*a.scale_factor)),
        "products":max(100,int(5_000*a.scale_factor)),
        "reps":max(50,int(2_000*a.scale_factor)),
        "orders":max(1_000,int(1_000_000*a.scale_factor)),
        "interactions":max(1_000,int(1_000_000*a.scale_factor)) }
    def dump(name,fields,rows):
        with (out/f"{name}.csv").open("w",newline="",encoding="utf-8") as f:
            z=csv.writer(f); z.writerow(fields); z.writerows(rows)
    dump("customers",["customer_id","segment","region","signup_date","status","acquisition_channel"],
         [[f"C{i:06d}",random.choice(["Consumer","SMB","Mid-Market","Enterprise"]),
           random.choice(["North","Midlands","South","Europe"]),d(),
           random.choice(["Active","Inactive","Churned"]),random.choice(["Web","Partner","Sales","Referral"])]
          for i in range(1,n["customers"]+1)])
    dump("products",["product_id","category","unit_price","cost"],
         [[f"P{i:05d}",random.choice(["Software","Hardware","Services","Accessories","Subscription"]),
           round(random.uniform(20,5000),2),round(random.uniform(10,3500),2)]
          for i in range(1,n["products"]+1)])
    dump("sales_reps",["rep_id","region","team"],
         [[f"R{i:05d}",random.choice(["North","Midlands","South","Europe"]),
           random.choice(["Enterprise","SMB","Strategic","Inside Sales"])]
          for i in range(1,n["reps"]+1)])
    orders=[]
    for i in range(1,n["orders"]+1):
        orders.append([f"O{i:07d}",f"C{random.randint(1,n['customers']):06d}",
          f"P{random.randint(1,n['products']):05d}",f"R{random.randint(1,n['reps']):05d}",d(),
          random.randint(1,20),round(random.uniform(20,5000),2),
          random.choice([0,.05,.1,.15,.2,.3,1.05]),
          random.choice(["Completed","Completed","Cancelled","Returned","Pending"])])
    dump("orders",["order_id","customer_id","product_id","rep_id","order_date","quantity","unit_price","discount","status"],orders)
    interactions=[]
    for i in range(1,n["interactions"]+1):
        interactions.append([f"I{i:07d}",f"C{random.randint(1,n['customers']):06d}",
          f"R{random.randint(1,n['reps']):05d}",d(),
          random.choice(["Lead","Enquiry","Demo","Proposal","Converted","Support"]),
          random.choice(["Email","Phone","Web","Event","Partner"])])
    dump("interactions",["interaction_id","customer_id","rep_id","interaction_date","stage","channel"],interactions)
    print("Enterprise-scale target:",f"{sum(n.values()):,}+ records")
if __name__=="__main__": main()
