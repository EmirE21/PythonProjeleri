def frequency_counter(data_list):
    # Boş bir sözlük oluşturulur.
    frecuency_dict = {}
    for item in data_list:
        # Eğer öğe sözlükte varsa, değeri 1 artırılır; yoksa 1 olarak eklenir.
        if item in frecuency_dict:
            frecuency_dict[item] += 1
        else:
            frecuency_dict[item] = 1
    # Sonuç olarak oluşturulan sözlük döndürülür.
    return frecuency_dict
"""
Başlangıçta sözlük boştur. 
Listedeki itemler sözlükte yoksa, sözlüğe eklenmek için ondan artık 1 tane olduğu "else" kısmı ile tanımlanır. 
Listedeki her farklı item için bu yapılır. 
Ardından artık sözlükte önceden tanımlanan itemler olacağından "if" kısmı True olarak geçecektir ve bu sefer 1 olarak girilen sayı 1 artırılacaktır. 
Bu şekilde girilen listede hangi itemden kaç tane olduğu sözlüğe eklenmiş olur.
"""
string = input("Sayıları boşlukla ayırarak girin: ")  # Örnek: "5 10 15 20"
data_list = [int(number) for number in string.split()]
result = frequency_counter(data_list)
print(result)