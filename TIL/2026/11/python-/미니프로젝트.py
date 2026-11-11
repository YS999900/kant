# 쇼핑몰 프로젝트
class Item:
    next_id = 1 # 클래스 변수
    def __init__(self, item, price, stock):
        self.id = Item.next_id
        Item.next_id += 1

        self.item = item           # 상품명
        self.price = price         # 가격
        self.stock = stock         # 재고수량

    def __str__(self):
        return f"상품 : {self.item}, 가격 : {self.price:,}, 재고수량{self.stock}"

    def __repr__(self):
        return f"상품 : {self.item}, 가격 : {self.price:,}, 재고수량{self.stock}"

    # 판매 후 재고감소
    def decrease(self, amount):
        if amount <= 0:
            print("수량은 1개 이상이어야 합니다.")
            return False
        
        if self.stock < amount:
            print("재고가 부족합니다.")
            return False

        self.stock -= amount

        if self.stock == 0:
            print("품절되었습니다.")

        return True


class ShoppingCart:
    def __init__(self):
        self.bucket = {}
        self.discount = Discount()
 
    # 장바구니 넣기
    def add_item(self, item, amount):
        if amount <= 0:
            print("수량은 1개 이상이어야 합니다.")
            return

        # 기존 상품인지 확인
        current_amount = self.bucket.get(item, 0)

        # 재고 확인
        if current_amount + amount > item.stock:
            print(f"재고가 부족합니다. (담을 수 있는 수량: {item.stock - current_amount}개)")
            return
        
        # 수량 추가
        self.bucket[item] = current_amount + amount
        print(f"{item.item} {amount}개를 담았습니다.")  

    # 장바구니 빼기
    def remove_item(self, item, amount):
        # 상품이 장바구니에 있는지 확인
        if item not in self.bucket:
            print("장바구니에 없는 상품입니다.")
            return

        #수량 확인
        if amount <= 0:
            print("수량은 1개 이상이어야 합니다.")
            return

        current_amount = self.bucket[item]

        # 제거할 수량이 담긴 수량보다 많으면
        if amount > current_amount:
            print(f"제거할 수 있는 수량은 {current_amount}개 입니다.")
            return

        # 수량 감소
        self.bucket[item] -= amount

        # 남은 수량이 0개라면 상품 삭제
        if self.bucket[item] == 0:
            del self.bucket[item]
            print(f"{item.item}을(를) 장바구니에서 제거했습니다.")
        else:
            print(f"{item.item} {amount}개를 제거했습니다.")
    
    # 상품 목록 조회
    def show_item(self):
        return self.bucket

    #상품 합계
    def get_total(self):
        total = 0
        for item, amount in self.bucket.items():
            total += item.price * amount

        return total

    def apply_discount(self, discount):
        self.discount = discount
        print(f"[{self.discount}] 쿠폰을 적용헸습니다.")
    
    # 배송비 계산
    def get_shipping_fee(self):
        if not self.bucket:
            return 0

        total = self.get_total()
        discount = self.discount.discount_amount(total)

        after_discount = total - discount

        if after_discount >= 30_000:
            return 0
        else:
            return 3_000

    # 최종 결제 금액 계산
    def get_final_total(self):
        total = self.get_total()
        discount = self.discount.discount_amount(total)
        shipping_fee = self.get_shipping_fee()

        return total - discount + shipping_fee

    # 결재 처리
    def checkout(self):
        # 장바구니가 비어있는지 확인
        if not self.bucket:
            print("장바구니가 비어 있습니다.")
            return

        # 재고 확인
        for item, amount in self.bucket.items():
            if item.stock < amount: 
                print(f"{item.item}의 재고가 부족합니다.")
                return 

        # 결재 금액 계산
        total = self.get_total()
        discount = self.discount.discount_amount(total)
        shipping_fee = self.get_shipping_fee()
        final_total = self.get_final_total()

        # 영수증 출력
        print("-" * 40)

        for item, amount in self.bucket.items():
            print(f"{item.item} x {amount} : {item.price * amount:,}원")

        print("-" * 40)
        print(f"상품 합계: {total:,}원")
        print(f"할인 금액: -{discount:,}원 [{self.discount}]")
        print(f"배송비: {shipping_fee:,}원")
        print(f"결재 금액: {final_total:,}원")
        print("-" * 40)

        # 재고 감소
        for item, amount in self.bucket.items():
            item.decrease(amount)

        # 장바구니 초기화
        self.bucket.clear()

        # 쿠폰 초기화
        self.discount = Discount()

        print("결재가 완료 되었습니다. 감사합니다!")
 
# 할인 쿠폰 클래스 추가
class Discount:
    def discount_amount(self, total):
        return 0

    def __str__(self):
        return "쿠폰없음"

# 10% 할인
class RateDiscount(Discount):
    def __init__(self, rate=0.1, max_amount=5000):
        self.rate = rate
        self.max_amount = max_amount

    def discount_amount(self, total):
        discount = int(total * self.rate)
        return min(discount, self.max_amount)

    def __str__(self):
        return f"{self.rate:.0%} 할인 (최대 {self.max_amount:,}원)"

# 3,000원 할인
class FixedDiscount(Discount):
    def __init__(self, amount=3000, min_total=20000):
        self.amount = amount
        self.min_total = min_total

    def discount_amount(self, total):
        if total >= self.min_total:
            return self.amount
        else:
            return 0

    def __str__(self):
        return f"{self.amount:,}원 할인 ({self.min_total:,}원 이상 구매 시)"


        


# 상품 생성
item_1 = Item("무선 이어폰", 89_000, 3)
item_2 = Item("텀블러", 15_000, 10)
item_3 = Item("보조배터리", 32_000, 5)
item_4 = Item("마우스패드", 9_000, 0)
item_5 = Item("USB 허브", 18_000, 4)

items = [item_1, item_2, item_3, item_4, item_5]

# 장바구니 생성
cart = ShoppingCart()

def main():
    while True:
        print("-" * 45)
        print("1.상품목록 2.담기 3.빼기 4.장바구니 5.쿠폰 6.결제 q.종료")
        print("-" * 45)

        choice = input("선택: ").strip()

        if choice == "1":
            for item in items:
                if item.stock == 0:
                    stock_text = "품절"
                else:
                    stock_text = f"재고 {item.stock}개"

                print(f"{item.id}. {item.item} {item.price:,}원 ({stock_text})")

        elif choice == "2":
            try:
                item_id = int(input("상품 번호: "))
                amount = int(input("수량: "))
            except ValueError:
                print("숫자를 입력해주세요")
                continue

            selected_item = None

            for item in items:
                if item_id == item.id:
                    selected_item = item
                    break
            if selected_item is None:
                print("존재하지 않는 상품입니다.")
            elif selected_item.stock == 0:
                print("품절된 상품입니다.")
            else:
                cart.add_item(selected_item, amount)

        elif choice == "3":
            try:
                item_id = int(input("제거할 상품 번호: "))
                amount = int(input("제거할 수량: "))
            except ValueError:
                print("숫자를 입렬해주세요.")
                continue

            selected_item = None

            for item in items:
                if item_id == item.id:
                    selected_item = item
                    break

            if selected_item is None:
                print("존재하지 않는 상품입니다.")
            else:
                cart.remove_item(selected_item, amount)

        elif choice == "4":
            # 장바구니가 비어 있는지 확인
            if not cart.bucket:
                print("장바구니가 비어 있습니다.")
                continue

            print("-" * 40)

            # 장바구니 상품 출력
            for item, amount in cart.bucket.items():
                print(f"{item.item} x {amount} : {item.price * amount:,}원")

            print("-" * 40)

            #결재 정보 계산
            total = cart.get_total()
            discount = cart.discount.discount_amount(total)
            shipping_fee = cart.get_shipping_fee()
            final_total = cart.get_final_total()  

            print(f"상품 합계: {total:,}원")
            print(f"할인 금액: -{discount:,}원 [{cart.discount}]")
            print(f"배송비: {shipping_fee:,}원")
            print(f"결재 금액: {final_total:,}원")
            print("-" * 40)

        
        elif choice == "5":
            print("1. 쿠폰 없음")
            print("2. 10% 할인 (최대 5,000원)")
            print("3. 3,000원 할인 (20,000원 이상 구매 시)")

            coupon_choice = input("쿠폰 번호: ").strip()

            if coupon_choice == "1":
                 coupon = Discount()

            elif coupon_choice == "2":
                coupon = RateDiscount()

            elif coupon_choice == "3":
                coupon = FixedDiscount()

            else:
                print("존재하지 않는 쿠폰입니다.")
                continue

            cart.apply_discount(coupon)

        elif choice == "6":
            cart.checkout()


        elif choice == "q":
            print("쇼핑몰을 종료합니다.")
            break


        else:
            print("아직 구현되지 않은 메뉴입니다.")

        

# 프로그램 실행
if __name__ == "__main__":
    main()

# cart.add_item(item_3, 3)
# cart.add_item(item_2, 2)

# print(f"상품 합계: {cart.get_total():,}원")

# # 실제 쿠폰 적용하기
# coupon = RateDiscount()

# # 장바구니에 쿠폰 적용
# cart.apply_discount(coupon)

# # 상품 합계
# total = cart.get_total()

# # 할인 금액
# discount = cart.discount.discount_amount(total)

# print(f"상품 합계: {total:,}원")
# print(f"할인 금액: {discount:,}원")

# print(f"최종 결재 금액: {cart.get_final_total():,}원")

# print(f"결제 전 보조배터리 재고: {item_3.stock}")
# print(f"결제 전 텀블러 재고: {item_2.stock}")

# cart.checkout()

# print(f"결재 후 보조배터리 재고:{item_3.stock}")
# print(f"결재 후 텀블러 재고:{item_2.stock}")

# print(cart.show_item())

