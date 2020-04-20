#include <iostream>
#include <algorithm>
#include <string>
#include <memory>
#include <assert.h>

using namespace std;

//void selectionSort(int arr[], int n){
//    for(int i = 0;i<n;i++){
//        int minIndex = i;
//        for(int j=i+1;j<n;j++){
//            if(arr[j] < arr[minIndex])
//                minIndex=j;
//        }
//        swap(arr[i],arr[minIndex]);
//    }
//}

//int main(){

//    int a[10]={10,9,8,7,6,4,3,2,1};
//     cout<<a<<" ";
//    selectionSort(a,10);

//    for (int i = 0; i < 10; ++i) {
//        cout<<a[i]<<" ";

//    }
//    cout<<endl;
//    return 0;
//}


//int main(){

//    //****************************************************************************test for myself 指针和引用

////    int a = 100, b = -9;
////    float c = 3.14f;
////    int* d = &a;
////    float* e = &c;

////    cout<<"d的输出："<<d<<"e的输出："<<e<<endl;
////    int q = *d;
////    cout<<"（*d）的输出："<<(*d)<<"（*e）的输出："<<(*e)<<endl;
////    cout<<b<<endl;
////    cout<<&a<<endl;
////    cout<<q<<endl;
////    cout<<*d<<endl;


//    //****************************************************************************test for myself 指针数组和数组指针

////    int a[4] = {0x0,0xF,0x000000000,0x7FFFFFFF};
////    int* b[4]; // arry of pointers 指针的数组，其实是元素是指针的数组
////    int(*c)[4]; //a pointer to an arry  数组的指针，其实是指向数组的指针


////    c = &a;

////    for (int i =0;i<4;i++) {
////        b[i] = &a[i];
////    }

////    cout<<*(b[3])<<" "<<(*c)[3]<<endl;

//    //*************************************************************test for myself 常量指针（const pointer）和指针常量(pointer to const)
//    //关于const修饰的部分：1.看左侧最近的部分 2.如果左侧没有，则看右侧

////    char strHelloworld[] = {"helloworld1"};
////    cout<<&strHelloworld[0]<<endl;
////    char const* pStr1 = "helloworld2";  //const char* 指针可以修改，常量字符不能修改
////    char* const pStr2 = strHelloworld;  //指针不能修改。，可以修改指向的内存数据
////    char const* const pStr3 = "helloworld3";     //const char* const
////    pStr1 = strHelloworld;
//////    pStr2 = strHelloworld;  不可以修改
//////    pstr3 = strHelloworld;    不可以修改


////    unsigned int MAX_LEN = 12;
////    unsigned int len = strnlen_s(pStr2,MAX_LEN);
////    cout<<len<<endl;
////    for (unsigned int index = 0; index < len; ++index) {
//////        pStr1[index]+=1;
////        pStr2[index]+=1;
//////        pStr3[index]+=1;
////        cout<<*pStr2<<"  "<<pStr2<<" "<<&pStr2<<pStr2[index]<<endl;
////    }



//    //*************************************************************test for myself 指向指针的指针
////    int a = 10;
////    int* b = &a;
////    int** c = &b;

//    //*************************************************************test for myself 几种原始指针
//    //未初始化和非法指针：1.要确保它已经初始化

//    //NULL指针 一个特殊的指针变量，表示不指向任何东西
////    int* e = NULL;

////    int* pA = NULL;
////    pA = &a;
////    if(pA!=NULL){

////        cout<<*pA<<endl;
////    }
////    else {

////        pA = NULL;
////    }

//    //"野指针"：1.指针变量没有初始化，2.已经释放不用的指针没有置NULL，如delete和free之后的指针，3.指针操作超越了变量的作用范围

//    //*************************************************************test for myself 指针的基本运算
//    //& *

////    char ch = 'a';
////    //&操作符
////    //&ch = 97;        //&ch左值不合法
////    char* cp = &ch;    //&ch右值
////    cout<<(*cp)<<" "<<cp<<&cp<<endl;
////    //&cp = 97;          //&cp左值不合法
////    char** cpp = &cp;    //&cp右值
////    cout<<cpp<<endl;

//    //*操作符
////    *cp = 'e';         //*cp左值取变量ch位置
////    char ch2 = *cp;    //*ch右值取变量ch存储的值
////    cout<<ch2<<endl;
////    //*cp + 1 ='a';    //*cp+1左值不合法的位置
////    ch2 = *cp + 1;     //*cp+1右值取到的字符做ASCII码加一操作
////    *(cp+1) = 'd';     //*(cp+1)左值语法上合法，取ch后面位置
////    ch2 = *(cp+1);     //*(cp+1)右值语法上合法，取ch后面位置的值

//    //++ 与 --操作符  前置操作符与后置操作符
////    char* cp2 = ++cp;
////    char* cp3 = cp++;
////    char* cp4 = --cp;
////    char* cp5 = cp--;
////    cout<<cp2<<cp3<<cp4<<cp5<<endl;


////    //++cp2 = 97;
////    //cp2++ = 97;

////    *++cp2 = 98;
////    char ch3 = *++cp2;
////    *cp2++ = 98;
////    char ch4 = *cp2++;
////    cout<<ch3<<ch4<<endl;

////    int a = 1, b = 2;
////    int c,d;
////    c = a+++b;
////    char ch5 = ++*++cp;

//    //*************************************************************test for myself 堆栈
//    //先进后出 First In，Last Out
//    //先进先出 First In，First Out


//    cout<<"hello"<<endl;

//    return 0;
//}



                //*************************************************************test for myself 堆栈
//int a = 0;                  //全局初始化区（GVAR）
//int* p1 ;                    //全局未初始化区（bss）

//int main(){                         //(text)代码区
//    int b = 1;                          //(stack)栈区变量
//    char s[] = "abc";              //(stack)栈区变量
//    int* p2 = NULL;                        //(stack)栈区变量
//    //const char *p3 = "123456";            //123456\0在常量区，p3在（stack）栈区
//    char* p3 = s;
//    static int c = 0;               //全局（静态）初始化区
//    p1 = new int(10);               //（heap）堆区变量
//    p2 = new int(20);               //（heap）堆区变量
//    char* p4 = new char[7];         //(heap)堆区变量
//    strcpy_s(p4,7,"123456");        //（text）代码区

//    if(p2 != NULL){    //nullptr
//        delete p2;
//        p2 = NULL;
//    };
//    if(p1 != NULL){
//        delete p1;
//        p1 = NULL;
//    };
//    if(p4 != NULL){
//        delete[] p4;
//        p4 = NULL;
//    };

//    //内存泄漏问题


//    cout<<b<<p2<<p3<<p4<<s<<c<<endl;
//    return 0;                   //(text)代码区
//}


            //*************************************************************test for myself 智能指针
            //unique_ptr、shared_ptr、weak_ptr  auto_ptr(C++17被正式删除)
//auto_ptr  存在所属权转移问题
//int main(){
//    {

//        auto_ptr<int> p1(new int(10));
//        cout<<*p1<<endl;


//        auto_ptr<string> codename[5] = {
//            auto_ptr<string>(new string("C")),
//            auto_ptr<string>(new string("jave")),
//            auto_ptr<string>(new string("C++")),
//            auto_ptr<string>(new string("python")),
//            auto_ptr<string>(new string("Cool")),

//        };


//        cout<<"first:\n";
//        for(int i=0;i<5;i++){
//            cout<<*codename[i]<<endl;

//        }

//        auto_ptr<string> pC;
//        pC = codename[2];

//        cout<<"second:\n";
//        for(int i=0;i<2;i++){
//            cout<<*codename[i]<<endl;

//        }
////        cout<<"所有权转移:\n";
////        for(int i=0;i<5;i++){
////            cout<<*codename[i]<<endl;

////        }

//        cout<<*pC<<endl;


//    }
//    return 0;
//}

//unique_ptr
//int main(){

//    {
//        auto i = unique_ptr<int>(new int(100));
//        cout<<i<<*i<<endl;

//    }

//    auto w = std::make_unique<int>(10);
//    cout<<*(w.get())<<endl;
//    //auto w2 = w;

//    //移动语义
//    auto w2 = std::move(w);
//    cout<<((w.get()!=nullptr)?(*w.get()):-1)<<endl;
//    cout<<((w2.get()!=nullptr)?(*w2.get()):-1)<<endl;
//    return 0;
//}


//shared_ptr
//int main(){

//    {   //共享所有权
//        auto wA = shared_ptr<int>(new int(20));
//        {
//            auto wA2 = wA;
//            cout<<((wA2.get()!=nullptr)?(*wA2.get()):-1)<<endl;
//            cout<<((wA.get()!=nullptr)?(*wA.get()):-1)<<endl;
//            cout<<wA2.use_count()<<endl;
//            cout<<wA.use_count()<<endl;
//        }
//        cout<<wA.use_count()<<endl;
//        cout<<((wA.get()!=nullptr)?(*wA.get()):-1)<<endl;
//    }

//    //move语法
//    auto wAA = std::make_shared<int>(30);
//    auto wAA2 = std::move(wAA);
//    cout<<((wAA.get()!=nullptr)?(*wAA.get()):-1)<<endl;
//    cout<<((wAA2.get()!=nullptr)?(*wAA2.get()):-1)<<endl;
//    cout<<wAA.use_count()<<endl;
//    cout<<wAA2.use_count()<<endl;


//    return 0;
//}


            //*************************************************************test for myself 循环引用问题机解决
//struct B;
//struct A{
//    shared_ptr<B> pb;
//    ~A(){cout<<"~A()"<<endl;}
//};
//struct B{
//    shared_ptr<A> pa;
//    ~B(){cout<<"~B()"<<endl;}

//};


//struct BW;
//struct AW{
//    shared_ptr<BW> pb;
//    ~AW(){cout<<"~AW()"<<endl;}
//};
//struct BW{
//    weak_ptr<AW> pa;
//    ~BW(){cout<<"~BW()"<<endl;}

//};

//void test(){
//    cout<<"两个都是shared_ptr"<<endl;
//    shared_ptr<A> tA(new A());
//    shared_ptr<B> tB(new B());
//    cout<<tA.use_count()<<endl;
//    cout<<tB.use_count()<<endl;
//    tA->pb = tB;
//    tB->pa = tA;
//    cout<<tA.use_count()<<endl;
//    cout<<tB.use_count()<<endl;


//}


//void test2(){
//    cout<<"shared_ptr和weak_ptr"<<endl;
//    shared_ptr<AW> tA(new AW());
//    shared_ptr<BW> tB(new BW());
//    cout<<tA.use_count()<<endl;
//    cout<<tB.use_count()<<endl;
//    tA->pb = tB;
//    tB->pa = tA;
//    cout<<tA.use_count()<<endl;
//    cout<<tB.use_count()<<endl;

//}

//int main(){

//    test();
//    test2();
//    return 0;
//}


            //*************************************************************test for myself 引用
            //引用是一种的特殊的指针，不允许修改的指针
            //指针的坑：空指针，野指针，不知不觉更改了指针的值还继续使用
            //使用引用：不存在空引用，必须初始化，一个引用永远指向它初始化的那个对象

//引用的基本使用：可以认为是指定变量额别名，使用时可以认为是变量本身

void swap(int& a, int& b){
    int tmp = a;
    a = b;
    b =tmp;

}

void swap2(int* a, int* b){
    int tmp = *a;
    *a = *b;
    *b =tmp;

}


int main(){
    int a=2,b=5;
    swap(a,b);
    cout<<a<<b<<endl;
    swap2(&a,&b);
    cout<<a<<b<<endl;
    assert(a==2&&b==5);

    return 0;
}

//有了指针为什么还需要引用：支持运算符重载
//有了引用为什么还需要指针：为了兼容C


//函数传递参数类型说明：内置基础类型传值更高效(pass by value)，面向对象中的自定义传递引用更高效（pass by reference const）

































