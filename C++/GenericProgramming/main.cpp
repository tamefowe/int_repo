#include <iostream>
#include <memory>
#include <string>

template <class T>
struct OpNewCreator
{
    static T* Create()
    {
        return new T("OpNewCreator");
    }
};


template <class T>
struct MallocCreator
{
    static T* Create()
    {
        void *buf = std::malloc(sizeof(T));
        if (!buf) return nullptr;
        return new (buf) T("MallocCreator");
    }
};


template <class T>
struct PrototypeCreator
{
    explicit PrototypeCreator(T *pObj = nullptr) : pPrototype_(pObj) {}

    T* Create()
    {
        return pPrototype_ ? pPrototype_->Clone(): nullptr;
    }

    T* GetPrototype()
    {
        return pPrototype_;
    }

    void SetPrototype(T* pObj)
    {
        pPrototype_ = pObj;
    }

private:
    T* pPrototype_;

};

struct Widget {

    explicit Widget(std::string m)
    : m_(move(m))
    {}
    void get()
    {
        std::cout << "widget : " << m_ << "\n";
    }

    Widget * Clone() {

        auto m = static_cast<Widget*>(this);
        return new Widget(*m);
    }

private:
    std::string m_;
};

template <template <class> class CreationPolicy>
class WidgetManager : public CreationPolicy<Widget>
{
public:
    void DoSomething()
    {
        Widget* pW = CreationPolicy<Widget>().Create();
        pW->get();
        delete pW;
    }

};

typedef WidgetManager<OpNewCreator> NewMgr;
typedef WidgetManager<MallocCreator> MallocMgr;
typedef WidgetManager<PrototypeCreator> PrototypeMgr;


int main() {

    NewMgr().DoSomething();

    MallocMgr().DoSomething();

    //PrototypeMgr().DoSomething();

    PrototypeMgr pm;
    //new Widget("initial widget"));
    Widget * wg = new Widget("new Prototype");
    pm.SetPrototype(wg);
    pm.DoSomething();

    return 0;
}
