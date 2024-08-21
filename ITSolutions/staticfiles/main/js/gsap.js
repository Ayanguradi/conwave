 gsap.registerPlugin(ScrollTrigger);

    gsap.utils.toArray("section").forEach((section, index, sections) => {
      const text = section.querySelector(".text");
      const image = section.querySelector(".image");

      gsap.fromTo(text, {
        y: 50,
        autoAlpha: 0
      }, {
        y: 0,
        autoAlpha: 1,
        duration: 1,
        scrollTrigger: {
          trigger: section,
          start: "top center",
          end: "bottom center",
          scrub: true
        }
      });

      gsap.fromTo(image, {
        y: 50,
        autoAlpha: 0
      }, {
        y: 0,
        autoAlpha: 1,
        duration: 1,
        scrollTrigger: {
          trigger: section,
          start: "top center",
          end: "bottom center",
          scrub: true
        }
      });

      if (index !== sections.length - 1) {
        ScrollTrigger.create({
          trigger: section,
          start: "top top",
          end: "bottom top",
          pin: true,
          pinSpacing: false,
          scrub: true,
          onLeave: () => gsap.to(section, { autoAlpha: 0, duration: 0.5 }),
          onEnterBack: () => gsap.to(section, { autoAlpha: 1, duration: 0.5 }),
        });
      }
    });


    // <!-- ------menu bar----- -->

      // $(window).scroll(function () {
      //   if ($(this).scrollTop() > 50) {
      //     $('.navbar').addClass('scrolled');
      //   } else {
      //     $('.navbar').removeClass('scrolled');
      //   }
      // });

      // $(document).ready(function () {
      //   $('.nav-link').on('click', function () {
      //     $('.nav-link').removeClass('active');
      //     $(this).addClass('active');
      //   });
      // });


// -- -----------------About header flip animation------------------ --

